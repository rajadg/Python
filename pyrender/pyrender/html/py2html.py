'''
Created on 02-Aug-2015

@author: dgraja
'''

import os
import sys
from tokenize import generate_tokens

from Node import span, tag, Html, para, pre, h1, h2, table, tr, td, Content


__py_token_map__ = {
    0 : None, 1 : 'id', 2 : 'num', 3 : 'str', 
    4 : 'spc', 5 : 'spc', 6 : 'spc',
    51: 'op', 53: 'cm', 
    101 : 'key', 102 : 'blt'}


__keywords__ = [ 'import', 'from', 'def', 'return', 'continue', 'pass', 
                'break', 'if', 'else', 'elif', 'for', 'range', 'in', 'not',
                'with', 'as', 'None', 'class', 'self', 'super', 'is', 
                'try', 'except', 'catch', 'final', 'raise' ]


__std__ = [ '__file__', '__name__', 'type', '__class__', '__init__' ]


def read_file(file_path):
    with open(file_path, 'r') as fp:
        return fp.read()


class py2html(object):
    '''
    Convert a python program to a readable html file with line numbers
    '''

    def __init__(self, python_source):
        '''
        Constructor
        '''
        self.__dir__ = os.path.dirname(__file__)
        css_file = os.path.join(self.__dir__, 'style_py.css')
        self.__style_python__ = read_file(css_file)
        self.__lines__ = dict()
        self.line_width = 80
        self.line_start = 0
        self.content_start = 0
        self.white_space = { 'class' : 'spc' }
        self.python_source = python_source
        if not os.path.exists(python_source):
            raise Exception("file: %s not found" % python_source)
        self.tokens = []
        self.read_tokens()
        self.break_points = []
        self.active_break_points = []
        self.current_line = -1
        
    def get_style_tag(self):
        return "<style type='text/css'>" + self.__style_python__ + "</style>"

    def css_style(self, token):
        '''
            Return the css style class for the token as dictionary
        '''
        ttype = token[0]
        if ttype == 1 and token[1] in __keywords__:
            ttype = 101
        elif token[0] == 1 and token[1] in __std__:
            ttype = 102
        cls = None
        if ttype in __py_token_map__:
            cls = __py_token_map__[ttype]
        if not cls:
            return None
        return {'class' : cls}    
        
    def lines(self):
        return self.__lines__
        
    def gen_tag(self, content, lineno, style):
        result = span(attrs=style)
        result.append(content.replace(' ', '&nbsp;'))
        if not lineno in self.lines():
            self.lines()[lineno] = []
        self.lines()[lineno].append(result)
        return result

    def make_tag(self, token, prev):
        '''
        Make a tag for the current token and then append to the current line
        @param token: The token from tokenizer
        @param lines: A dictionary where the keys are line numbers. The value
                    is a list of html tag instances
        @param prev: The previous token from tokenizer 
        '''
        style = self.css_style(token)
        (ttype, content, start, end, txt) = token
        
        prefix = ''
    
        # current token same line as previous token
        if prev:
            prev_end =  prev[3]
            # reset the line_start & content_start for line-wrap of long lines
            if prev_end[0] < start[0]:
                self.line_start = 0
                self.content_start = start[1]
            # Check if previous token is same line or previous line
            if prev_end[0] < start[0] and start[1] != 0:
                # reset prev_end to current line @ col 0
                prev_end = (start[0], 0)
            if prev_end[0] == start[0]:
                # If there is a gap previous token and current token
                # the gap is a whitespace gap
                if prev_end[1] < start[1]:
                    # Compute the required whitespaces and insert them to html
                    diff = start[1] - prev_end[1]
                    prefix = '&nbsp;' * diff
                    self.gen_tag(prefix, start[0], self.white_space)
        
        # Handle the strings
        if end[0] > start[0]:
            if ttype != 3:
                print "token error: %r" % (token)
                return
            # split the string token into individual lines
            items = content.split('\n')
            lineno = start[0]
            # generate one tag per line
            for line in items:
                self.gen_tag(line, lineno, style)
                lineno = lineno+1
        else:
            # Check if the long line needs to be wrapped
            if end[1] > self.line_width:
                if end[1] - self.line_start > self.line_width and end[0] == start[0]:
                    self.line_start = end[1]
                    next_line = "<br/>" + '&nbsp;' * (self.content_start + 4)
                    content = next_line + content
            # generate a tag for the content and style
            self.gen_tag(content, start[0], style)          
        return
    
    def read_tokens(self):
        '''
            Read the tokens from the file into an array
        '''
        with open(self.python_source, 'r+') as fp:
            generator = generate_tokens(fp.readline)
            for tpl in generator:
                self.tokens.append(tpl)
        
        prev = None
        for token in self.tokens:
            self.make_tag(token, prev)
            prev = token
        return

    def get_full_html(self):
        '''
            Return the python program as full html
        '''
        content = Html(title=str(self.python_source))
        content.head().append(self.get_style_tag())
        content.body().append(self.get_html_table())
        return content
        
    def get_html_table(self):
        '''
            Get the python program as simple html table
        '''
        tbl = table()
    
        for key in sorted(self.lines().keys()):
            row = tr()
            extra_style = ''
            if key == self.current_line:
                extra_style = ' current_line'
            elif key in self.active_break_points:
                extra_style = ' active_break_point'
            elif key in self.break_points:
                extra_style = ' break_point'
            row.append(td(children=[str(key), 
                                    Content(tag_name='a', attrs = { 'name' : str(key)} ) ], 
                          attrs={'class': 'lineno' + extra_style}))
            row.append(td(children=self.lines()[key], 
                          attrs={'class': 'fill' + extra_style}))
            tbl.append(row)
            
        return tbl
        
    def render_html_table(self):
        '''
            Renders the python program as simple html table
        '''
        tbl = self.get_html_table()
        return str(tbl)

    def save_as_html(self, target):
        '''
            Saves the python source as colorful HTML
        '''
        content = self.get_full_html()
        with open(target, 'w') as fp:
            fp.write(str(content))
        return
    
    
def main():
    obj = py2html("D:\\temp\\target.py")
    obj.current_line = 11
    obj.break_points = range(0,125, 5)
    obj.active_break_points = [10, 15, 30, 55, 60]
    obj.save_as_html("D:\\temp\\out.html")
    
        
if __name__ == '__main__':
    main()
    pass 

'''
Created on 20-Mar-2015

@author: dgraja
'''

import os
from datetime import datetime
import time

class LoggerHtml(object):
    '''
    A logger class to log in html format
    '''
    def __init__(self, file_name='logfile', folder=None, use_time_stamp=True, append=False, title='Sample Log', style=None):
        '''
        Constructor
        '''
        self.folder = self.default_folder(folder)
        self.file_name = file_name + (datetime.now().strftime("_%Y%m%d_%H.%M.%S") if use_time_stamp else "") + ".html"
        self.location = os.path.join(self.folder, self.file_name)
        self.append = append
        print self.location
        if os.path.exists(self.location) and not append:
            os.unlink(self.location)
        with open(self.location, 'w') as fp:
            fp.write("<html>")
        
        self.write(self.make_tag('head', self.make_tag('title', title)))
        self.open_tag('body', style=style)
        
    def default_folder(self, folder=None):
        if not folder:
            folder = os.path.join(os.environ('HOME'), 'temp')
        if not os.path.exists(folder):
            os.mkdir(folder)
        return folder
        
    def timestamp(self):
        return datetime.now().strftime("[%Y-%m-%d %H:%M:%S.%f] ")
        
    def write(self, text):
        '''
            Write the given text to the file
            @param text: the text to write to the log file
        '''
        with open(self.location, 'a') as fp:
            fp.write(text)

    def write_content(self, content, wrapper=None):
        ''' 
            Write the given content with outer tag to log file 
            @param content: The content to write to the log file
            @param wrapper: The outer html tag surround this tag as a tuple. example: ("<a name='intro'>", "</a>") for wrapping a tag inside an anchor
        '''
        text = content
        if wrapper and (isinstance(wrapper, tuple) or isinstance(wrapper, list)) and len(wrapper)>1:
            text = wrapper[0] + " " + text + " " + wrapper[1]
        self.write(text)
    
    def write_tag(self, tag_name, content, style="", color=None, size=None, font=None, bg_color=None, attrs="", wrapper=None):
        '''
            Writes a give tag in html format to the log file
            @see: make_tag for more details on params
        '''
        self.write(self.make_tag(tag_name, content, style, color, size, font, bg_color, attrs, wrapper))
        
    def make_tag(self, tag_name, content, style="", color=None, size=None, font=None, bg_color=None, attrs="", wrapper=None):
        '''
            Makes a Html tag for writing to log file
            @param tag_name: The name of the tag (ex: h1, h2, span, p, div, etc)
            @param content: The content to write within the tag
            @param style: The style of the tag (ex: color: red)
            @param color: The color of the content (ex: green, blue)
            @param size: The font size of the content
            @param font: The font of the content (ex: arial, verdana, georgia, cambria, courier, etc)
            @param attrs: The list of attributes as dictionary or a simple string
                1. string example: height='10' width='10'
                2. dictinoary example: { 'cellpadding' : 0, 'cellspacing' : 0, 'border' : '1' }
            @param wrapper: The outer html tag surround this tag as a tuple. example: ("<a name='intro'>", "</a>") for wrapping a tag inside an anchor
            
            @return A complete html string for this tag
            
        '''

        return self.wrap_content( content="<%s %s %s>%s</%s>" % (tag_name, 
                                        self.make_style(style, color, size, font, bg_color), 
                                        self.make_attrs(attrs), 
                                        content, 
                                        tag_name),
                                   wrapper=wrapper)
        
    def open_tag(self, tag_name, style="", color=None, size=None, font=None, bg_color=None, attrs=""):
        ''' Open a tag for writing inside. example: table, list '''
        self.write(text="<%s %s %s>" % (tag_name, 
                                        self.make_style(style, color, size, font, bg_color), 
                                        self.make_attrs(attrs)))
    def close_tag(self, tag_name):
        ''' Close a tag after writing contents '''
        self.write(text=' </%s>' % tag_name)
        
    def make_style(self, style="", color=None, size=None, font=None, bg_color=None):
        '''
            Makes a style attribute
            @param style: The style of the tag (ex: color: red)
            @param color: The color of the content (ex: green, blue)
            @param size: The font size of the content
            @param font: The font of the content (ex: arial, verdana, georgia, cambria, courier, etc)
            @return the style attribute string in the form style="..." or empty string
        '''
        if not style:
            style = ""
        if color:
            style = style + "; color: %s" % color
        if bg_color:
            style = style + "; background-color: %s" % bg_color
        if size:
            style = style + "; font-size: %s" % size
        if font:
            style = style + "; font-family: %s" % font
            
        if len(style) > 0:
            style = "style='%s' " % style
        return style
    
    def make_attrs(self, attrs=''):
        ''' 
        Construct the attribute string to be ready for use in a tag
            @param attrs: The list of attributes as dictionary or a simple string
                1. string example: height='10' width='10'
                2. dictinoary example: { 'cellpadding' : 0, 'cellspacing' : 0, 'border' : '1' }
            @return the attribute string in html format
        '''
        if isinstance(attrs, dict):
            attrs = " ".join(["%s='%s'" % (key, str(attrs[key])) for key in attrs.keys()])
    
    def wrap_content(self, content, wrapper=None):
        '''
        Wraps html content inside another html tag
            @param conent: the content to wrap
            @param wrapper: The outer html tag surround this tag as a tuple. example: ("<a name='intro'>", "</a>") for wrapping a tag inside an anchor
            @return The wrapped content
        '''
        if wrapper and (isinstance(wrapper, tuple) or isinstance(wrapper, list)) and len(wrapper)>1:
            return wrapper[0] + " " + content + " " + wrapper[1]
        return content

    def make_para(self, content, color=None, size=None, font=None, bg_color=None):
        ''' Make a para tag '''
        return self.make_tag('p', self.timestamp() + str(content), style='', color=color, size=size, font=font, bg_color=bg_color)
    
    def para(self, content, color=None, size=None, font=None, bg_color=None):
        ''' Write a para tag '''
        self.write(self.make_para(content, color=color, size=size, font=font, bg_color=bg_color))
    
    def highlight(self, content, color='blue', size='large', font=None, wrapper=None):
        ''' Make a para highlighted '''
        self.span(content, style='', color=color, size=size, font=font, bg_color='yellow', wrapper=wrapper)
    
    def heading(self, content, level=1, style=None, color='black', font=None, size=None, bg_color=None, wrapper=None):
        self.write(self.make_tag('h%d' % level, content, style='', color=color, size=size, font=font, bg_color=bg_color, wrapper=wrapper))
    
    def span(self, content, style=None, color=None, font=None, size=None, bg_color=None, wrapper=None):
        self.write(self.make_tag('span', content, style='', color=color, size=size, font=font, bg_color=bg_color, wrapper=wrapper))
    
    def div(self, content, style=None, color=None, font=None, size=None, bg_color=None, wrapper=None):
        self.write(self.make_tag('div', content, style='', color=color, size=size, font=font, bg_color=bg_color, wrapper=wrapper))
    
    def info(self, content, size=None, font=None):
        self.para(content, 'darkgray', size, font)

    def bulkdata(self, content, size=None, font=None):
        self.para(content, color='silver', size='small', font=font)
    
    def warn(self, content, size=None, font=None):
        self.para(content, 'blue', size, font)
    
    def error(self, content, size=None, font=None):
        self.para(content, 'red', size, font)
        
    def anchor(self, id):
        self.write("\r\n<a name='%s'>" % id)
        
    def make_row(self, items):
        result = "\r\n<tr>"
        for item in items:
            result = result + "<td>%s</td>" % str(item)
        return result + "</tr>"
        
        
def main():
    #print check_db_exists('Clouddesk_HF42')
    log = LoggerHtml(file_name = 'test', 
                     folder='/Users/dgraja/working/temp',
                     style='background-color: #f7fff7; font-size: medium; font-family: courier')
    try:
        log.heading("Sample Log", style='color: blue')
        log.para("first line in brown color and x-large font size", color='brown', size='x-large')
        log.write("calling log.write with default color")
        time.sleep(1.3)
        log.para("calling log.para with green color", 'green')
        time.sleep(1.3)
        log.warn("this is done using log.warn")
        time.sleep(0.7)
        log.info("this is done using log.info")
        time.sleep(0.6)
        log.error("this is done using log.error")
        time.sleep(1.8)
        log.bulkdata("this is done using ......... log.bulkdata")
        time.sleep(0.4)
        log.highlight("this is done by log.hightlight")
        
        log.open_tag('table', bg_color='#eff7ff', attrs= {'cellpading' : 0, 'cellspacing' : 0, 'border' : 2} , style='border: solid 1px blue')
        log.open_tag('tr', size='x-large', style='height: 30px')
        log.write_tag('td', 'sno', style='width: 80px')
        log.write_tag('td', 'file-name', style='width: 300px')
        log.write_tag('td', 'last-modified', style='width: 200px')
        log.write_tag('td', 'size', style='width: 100px')
        log.close_tag('tr')
        
        log.write(log.make_row(['1', 'test.txt', '2015-03-10 16:01:00 IST', '200kb']))
        log.write(log.make_row(['2', 'sample.jpg', '2015-02-10 06:34:31 IST', '1mb']))
        log.write(log.make_row(['3', 'image.png', '2015-03-12 22:03:40 IST', '500kb']))
        
        log.close_tag('table')
        
    except Exception, e:
        print e
    
    os.system("open " + log.location)

    return

if __name__ == '__main__':
    main()
    pass'''


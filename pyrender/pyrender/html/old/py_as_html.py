'''
Created on 02-Aug-2015

@author: dgraja
'''


from Node import span, tag, Html, para, h1, h2, table, tr, td, Content
from css_resource import css_style, white_space, get_style_tag
from tokenize import generate_tokens

import datetime
import time

def gen_tag(content, lineno, lines, style):
    result = span(attrs=style)
    result.append(content.replace(' ', '&nbsp;'))
    if not lineno in lines:
        lines[lineno] = []
    lines[lineno].append(result)
    return result
    

line_width = 80
line_start = 0
content_start = 0

def make_tag(token, lines, prev):
    global line_start
    global line_width
    global content_start
    style = css_style(token)
    (ttype, content, start, end, txt) = token
    
    prefix = ''

    # current token same line as previous token
    if prev:
        prev_end =  prev[3]
        if prev_end[0] < start[0]:
            line_start = 0
            content_start = start[1]
        if prev_end[0] < start[0] and start[1] != 0:
            prev_end = (start[0], 0)
        if prev_end[0] == start[0]:
            if prev_end[1] < start[1]:
                diff = start[1] - prev_end[1]
                prefix = '&nbsp;' * diff
                gen_tag(prefix, start[0], lines, white_space())
    
    # Handle the strings
    if end[0] > start[0]:
        if ttype != 3:
            print "token error: %r" % (token)
            return
        items = content.split('\n')
        lineno = start[0]
        for line in items:
            gen_tag(line, lineno, lines, style)
            lineno = lineno+1
    else:
        if end[1] > line_width:
            if start[0] > 100:
                pass
            if end[1] - line_start > line_width and end[0] == start[0]:
                line_start = end[1]
                next_line = "<br/>" + '&nbsp;' * (content_start + 4)
                content = next_line + content
        gen_tag(content, start[0], lines, style)
            
    return None


def read_tokens(target_file=r"d:\temp\target.py"):
    tokens = []
    with open(target_file, 'r+') as fp:
        generator = generate_tokens(fp.readline)
        for tpl in generator:
            tokens.append(tpl)
    return tokens




def main():
    
    start = datetime.datetime.now()
    lines = dict()
    tokens = read_tokens()
    prev = None
    for token in tokens:
        make_tag(token, lines, prev)
        prev = token
#         print token
    
    content = Html()
    content.head().append(get_style_tag())
#     content.body().append(h2('source code'))
    tbl = table()
    content.body().append(tbl)

    for key in sorted(lines.keys()):
        row = tr()
        row.append(td(children=str(key), attrs={'class': 'lineno'}))
        row.append(td(children=lines[key], attrs={'class': 'fill'}))
        tbl.append(row)
        
    with open(r'D:\temp\\out.html', 'w') as fp:
        content.write_to(fp)

    time.sleep(1)
    duration = datetime.datetime.now() - start
    print duration

if __name__ == '__main__':
    main()
    pass
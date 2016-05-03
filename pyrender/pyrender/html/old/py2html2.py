'''
Created on 02-Aug-2015

@author: dgraja
'''

from pyrender.html.Node import *
import json
from tokenize import generate_tokens

_token_types_ = {}

__token_colors__ = { 
                    52: 'darkblue',
                    3: 'darkgreen',
                    51: 'blue',
                    2: 'magenta',
                    1: 'brown',
                    53: 'gray',
                    -1 : 'brown',
                    101: 'darkcyan'
              }

__keywords__ = [ 'import', 'from', 'def', 'return', 'continue', 'pass', 
                'break', 'if', 'else', 'elif', 'for', 'range', 'in', 'not',
                'with', 'as', 'None', 'class', 
                'try', 'except', 'catch', 'final', 'raise' ]

__std__ = [ '__file__', '__name__', 'type', '__class__', '__init__' ]

def token_style(token):
    ttype = -1;
    if token[0] in __token_colors__:
        ttype = token[0]
    
    if not token[0] in _token_types_:
        _token_types_[token[0]] = token
    
    if token[0] == 1 and token[1] in __keywords__:
        ttype = 51
        
    if token[0] == 1 and token[1] in __std__:
        ttype = 101
        
    return { 'style' : 'color: %s;' % __token_colors__[ttype] }


def read_tokens(target_file=r"d:\temp\target.py"):
    tokens = []
    with open(target_file, 'r+') as fp:
        generator = generate_tokens(fp.readline)
        for tpl in generator:
            tokens.append(tpl)
    return tokens


def token_text(token, line, linecount):
    result = ''
    if token[0] == 5:
        result = '&nbsp;'
    result = result + line.replace(' ', '&nbsp;')
    if linecount > 1:
        result = result + "\n<br/>"
    else:
        result = result + '&nbsp;'
    return result

def compose_token(token, lineno):
    if token[0] == 54 and token[1] == '\n':
        return '\b<br/>'
    lines = str(token[1]).split('\n')
    if not lines:
        return None
    if len(lines)==1:
        return [span(attrs=token_style(token)).append(token_text(token, lines[0], len(lines))), ]
    
    result = [span(attrs=token_style(token)).append(token_text(token, lines[0], 1))]
    for line in lines[1:]:
        result.append(span(attrs=token_style(token)).append(token_text(token, line, len(lines))))
    return result


def main():
    tokens = read_tokens()
    ret = Html()
    bd = ret.body()
    for tk in tokens:
        print tk
        for item in compose_token(tk, 0):
            bd.append(item)
    
    with open(r'D:\temp\\out.html', 'w') as fp:
        bd.write_to(fp)
        
    for key, val in _token_types_.iteritems():
        print "%r : %r" % ( key, val )

if __name__ == '__main__':
    main()
    pass


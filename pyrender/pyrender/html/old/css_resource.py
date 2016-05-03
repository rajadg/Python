'''
Created on 02-Aug-2015

@author: dgraja
'''


__py_css__ = '''

body {
    font-family: courier new;
}
table {
    width: 100%
}
td {
    border-left: solid 1px black;
}
.fill {
    width: 99%;
    text-wrap: unrestricted;
}
.lineno {
    color: darkcyan;
    width: 40px;
    text-align: right;
    font-weight: bold;
    padding-left: 5px;
    padding-right: 5px;
    vertical-align: top;   
}
.id {
    color: black;
}
.key {
    color: blue;
    font-weight: bold;
}
.num {
    color: magenta;
}
.op {
    color: blue;
    font-weight: bold;
}
.cm {
    color: gray;
}
.str {
    color: red;
}
.blt {
    color: darkblue;
}
.cst {
    color: darkcyan;
}
spc {
    white-space: pre;
}

'''


__py_token_map__ = {
    0 : None, 1 : 'id', 2 : 'num', 3 : 'str', 
    4 : 'spc', 5 : 'spc', 6 : 'spc',
    51: 'op', 53: 'cm', 
    101 : 'key', 102 : 'blt'}


__keywords__ = [ 'import', 'from', 'def', 'return', 'continue', 'pass', 
                'break', 'if', 'else', 'elif', 'for', 'range', 'in', 'not',
                'with', 'as', 'None', 'class', 'self', 'super', 
                'try', 'except', 'catch', 'final', 'raise' ]


__std__ = [ '__file__', '__name__', 'type', '__class__', '__init__' ]


def get_style_tag():
    return "<style type='text/css'>" + __py_css__ + "</style>"


def white_space():
    return { 'class' : 'spc' }

def css_style(token):
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





if __name__ == '__main__':
    pass






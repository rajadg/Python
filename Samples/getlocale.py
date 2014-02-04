import os

def local_environ():
    vars = ['LANGUAGE', 'LC_ALL', 'LC_TYPE', 'LANG']
    for v in vars:
        loc = os.environ.get(v)
        if loc: return loc
    else:
        return None


ret = local_environ()

print ret

import _locale
code, encoding = _locale._getdefaultlocale()

print code
print encoding

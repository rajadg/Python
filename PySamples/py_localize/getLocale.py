'''
Created on 03-Feb-2014

@author: dgraja
'''

import locale
import os


#
# 
# 
#
def local_environ():
    try:
        vars = ['LANGUAGE', 'LC_ALL', 'LC_TYPE', 'LANG']
        for v in vars:
            loc = os.environ.get(v)
            if loc: return loc
        else:
            return None
    except Exception as e:
        print e
    return None

#
# 
# 
#
def get_locale():
    default_loc = locale.getdefaultlocale()
    environ_loc = local_environ()
    loc = environ_loc or default_loc[0]
    lang = str(loc).split('_')[0]
    return loc, lang


print "Calling getLocale :"
print "Result: ", get_locale()

























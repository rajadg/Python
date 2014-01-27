'''
Created on 27-Jan-2014

@author: dgraja
'''

def decorator_class(my_class):
    def getinstance(*args, **kw):
        print "class " + my_class.__name__ + " is instantiated ..."
        return ('START', my_class(*args, **kw), 'END')
    return getinstance

@decorator_class
class point(object):
    '''
    Represents a 2D point
    '''
    def __init__(self, a=0, b=0):
        '''
            constructor for point
        '''
        self.a = a
        self.b = b
    
    def __str__(self):
        return "(" + str(self.a) + ", " + str(self.b) + ")"

import json

def test_class_01():
    pt = point(10,11)
    print "created point"
    for item in pt :
        if type(item).__name__ == 'str' :
            print item
        else:
            print str(item)
    
test_class_01()
    
    
    
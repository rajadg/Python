'''
Created on 27-Jan-2014

@author: dgraja
'''

Counter = 1
def decorator_class(my_class):
    def getinstance(*args, **kw):
        class derived_class(my_class):
            Counter = 1
            def __init__(self, *args, **kw):
                print "inside wrapper class for : " + str(my_class.__name__) + ", args: " + str(args)
                super(derived_class, self).__init__(*args, **kw)
                global Counter
                self.ID = Counter
                Counter = Counter + 1
        return derived_class(*args, **kw)
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
        print "inside constructor of point"
        self.a = a
        self.b = b
    
    def __str__(self):
        return "(" + str(self.a) + ", " + str(self.b) + ")"

def test_class_02():
    pt = point(30,31)
    pt2 = point(50,52)
    print str(pt) + ", ID:" + str(pt.ID)
    print str(pt2) + ", ID:" + str(pt2.ID)
    
test_class_02()
    
    
    
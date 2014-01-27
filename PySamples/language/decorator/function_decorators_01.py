'''
Created on 27-Jan-2014

@author: dgraja
'''

def func_deco(param):
    '''
        This is a wrapper. The 'param' is the argument explicitly passed to the decorator
    '''
    #print "inside func_deco. param: " + str(param)
    def wrapper(original_function):
        '''
            This method is the wrapper of the decorator. The original_function is the function
            that will be decorated
        '''
        #print "inside implementation. param: " + str(original_function)
        def proxy_implementation(*args, **kw):
            '''
                This is the proxy that takes same argument as original_function, and does something else
                usually this proxy does some additional and then call original_method
            '''
            #print "inside proxy_implementation. param: " + str(args) + ", " + str(kw)
            return original_function(*args, **kw)
        return proxy_implementation
    return wrapper


@func_deco(10)
def add_numbers_01(a, b):
    print "inside add_numbers: " + str(a) + ", " + str(b)
    return a + b

def test_func_01():
    print "Calling add_numbers..."
    print "result: " + str(add_numbers_01(23,24))
    print "finished !!" 
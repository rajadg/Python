'''
Created on 27-Jan-2014

@author: dgraja
'''

def log_to_console(original_function):
    '''
        This is a wrapper. The 'original_function' is method that is overriden by this decorator
    '''
    #print "inside implementation. param: " + str(original_function)
    def proxy_implementation(*args, **kw):
        '''
            This is the proxy that takes same argument as original_function, and does something else
            usually this proxy does some additional and then call original_method
        '''
        print "Begin method:" + str(original_function.__name__) + ". arguments: " + str(args) + ", " + str(kw)
        result = original_function(*args, **kw)
        print "End method:" + str(original_function.__name__) + ". result: " + str(result)
        return result 
    return proxy_implementation


@log_to_console
def add_numbers_02(a, b):
    print "inside add_numbers: " + str(a) + ", " + str(b)
    return a + b

def test_func_02():
    print "Calling add_numbers..."
    print "result: " + str(add_numbers_02(23,24))
    print "finished !!" 
    
test_func_02()
    
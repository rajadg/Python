'''
Created on Dec 9, 2013

@author: dgraja
'''


def mod2(x) :
    return x%2==0
    
'''
    The filter method is used to filter a list (or array) 

'''
even = filter(mod2, xrange(1,10))

print even
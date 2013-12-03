'''
Created on Nov 6, 2013

@author: dgraja
'''

integers = [ 1,2,3,4,5]
def square(i):
    return i*i

squares = map(square, integers)

print "All integers used : " + str(integers)
print "Computed squares (using map) : " + str(squares)


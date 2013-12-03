
''' 
This file contains sample code to work with tuples
'''

# Declare a simple tuple
existing_list = [1, 2, 3]
my_tuple = (1, 2, 3, 4, 5)
# print the contents of the tuple
print "my_tuple contents are :" + str(my_tuple)
# Create a tuple from a list object
print "tuple created from list :" + str(tuple(existing_list))

print 'class of my_tuple : ' + str(my_tuple.__class__)

'''
Example to that uses tuple for params to call a method

1. Define a method
2. Define a tuple with same params as the method
3. Call the method with tuple as params
4. print the result

'''
def multiply(a, b):
    return a * b
params_tuple = (11, 12)
result = multiply(*params_tuple)
print "result : " + str(result)



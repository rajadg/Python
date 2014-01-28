
'''
Create a list and manipulate the list

'''
my_list = [1, 2, 3, 4]

# Print the length
print str(my_list.__len__())

# Append another item to the list
my_list.append(5)
my_list.extend([6, 7, 8])
my_list.append([9, 10])
# print the list that is appended / extended
print "the contents of list is "
print my_list

print 'class of my_list : ' + str(my_list.__class__)


my_list.reverse()
# reversed list
print my_list

alphabets = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', ['i', 'j']]
alphabets.reverse()
combo = zip(alphabets, my_list)

print "zipped list (combo) is " + str(combo)
print 'class of combo : ' + str(combo.__class__)
print 'class of first element of combo : ' + str(combo[0].__class__)


# creating a string list for manipulation
str_list = [ 'first', 'second', 'third', 'fourth', 'fifth', 
            'sixth', 'seventh', 'eighth', 'ninth', 'tenth' ]

print " new list created : " + str(str_list)

print "first three items are : " + str(str_list[:3])
print "middle three items are : " + str(str_list[5:8])
print "last three items are : " + str(str_list[-3:])
print "two items preceding last: " + str(str_list[-3:-1])

print 'class of str_list : ' + str(str_list.__class__)

'''
Example to that uses list for params to call a method

1. Define a method
2. Define a list with same params as the method
3. Call the method with list as params
4. print the result

'''
def multiply(a, b):
    return a * b
params_list = [11, 12]
result = multiply(*params_list)
print "result : " + str(result)

big_list = [1,2,3,4,5,6,7,8,9,10]
# pass 8,9 from the list as arguments
result = multiply(*big_list[-3:-1])
print "result (from partial list): " + str(result)



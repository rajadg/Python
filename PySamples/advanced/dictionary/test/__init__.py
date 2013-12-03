
'''

Example to demonstrate a dictionary usage in python

'''

# Create a basic dictionary and print the contents
my_coll = { 
           'language' : 'python', 
           'module' : 'sync',
           'purpose' : 'synchronize with server',
           'standalone' : 'yes',
           'ui' : 'available',
           'windows' : 'yes',
           'mac'  : 'yes',
           'linux' : 'yes'
           }
# print the dictionary
print str(my_coll)

print "all keys:\n" + str(my_coll.keys())

print "all values:\n" + str(my_coll.values())

print 'item named purpose = ' + my_coll['purpose']

print 'class of my_coll : ' + str(my_coll.__class__)


'''
Example uses dictionary as method params
1. Define a concat method
2. method contains some named params which are available in dictionary
3. call the method with dictionary as params
'''

print "\n\n Demonstrate using dictionary as method params"
def concat(first, second):
    return first + ' ' + second

params_dictionary = { 'first' : 'Hello',
                     'second' : 'World'}

result1 = concat(**params_dictionary)
print "result of first time : " + result1

result2 = concat(first=result1, second='!!')
print "result of second time : " + result2

result_improper = concat(*params_dictionary)
print "result of improper call : " + result_improper





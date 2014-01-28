'''
Created on Nov 6, 2013

Sample containing list comprehension


@author: dgraja
'''

'''
Compute squares of all numbers between 1 and 10
'''
# compute squares
squares = [ x ** 2 for x in range(10)]
print "squares computed (list comprehension): " + str(squares)
# alternate long syntax
squares = []
for x in range(10):
    squares.append(x ** 2)
print "squares computed (using lot of code): " + str(squares)

#squares using lambda
squares = map(lambda x:x**2, range(10))
print "squares computed (using lambda): " + str(squares)


'''
compute squares for all odd numbers between 1 to 10
'''
odd_squares = [x ** 2 for x in range(10) if x % 2 != 0]
print "odd squares computed (list comprehension): " + str(odd_squares)
# alternate long syntax
odd_squares = []
for x in range(10):
    if x % 2 != 0 :
        odd_squares.append(x ** 2)
print "odd squares computed (using lot of code): " + str(odd_squares)


'''

A crazy prime number generation example using list comprehension

10,000 is an optimal max_limit. This code cannot go beyond 10,000.

'''
import math

max_limit = 1100
root = int( math.sqrt(max_limit))
# get all non primes
non_primes = [j for i in range(2, root) for j in range(i * 2, max_limit, i) ]
# get all numbers between 1 and max_limit ** 2 that are not in non_primes
primes = [x for x in range(2, max_limit) if x not in non_primes]

print "all numbers prime until max_limit : " + str(primes)


def filter_max(list, max):
    return [x for x in list if x < max]

powers = [10**x for x in range(0,6)]
print "powers is " + str(powers)
print "total prime numbers is " + str(primes.__len__())

for limit in powers :
    print "limiting for " + str(limit)
    print "total is " + str(filter_max(primes, limit).__len__())




'''
Created on Dec 9, 2013

@author: dgraja
'''


'''
    This snippet demonstrates the all and any functions
'''
print "\n\nDemo 'all' & 'any'"

list_all = range(1,11)
list_even = range(0,11,2)
list_odd = range(1,11,2)

def check_list(target_list):
    if all([i%2==0 for i in target_list]) :
        print "The list " + str(target_list) + " contains only even numbers ('all' function returns success)"
    elif any([i%2==0 for i in target_list]) :
        print "The list " + str(target_list) + " contains some even numbers ('any' function returns success)"
    else :
        print "The list " + str(target_list) + " does not contain any even number ('all' & 'any' functions failed)"

check_list (list_all)
check_list (list_even)
check_list (list_odd)


'''
    This snippet demonstrates the abs function
'''
print "\n\nDemo 'abs'"

target = -10.3
print "Absolute value of " + str(target) + " is " + str(abs(target))


'''
    This snippet demonstrates the bin function
'''
print "\n\nDemo 'bin'"

target = 14
print "Bin value of " + str(target) + " is " + str(bin(target))
print "Bin [2:] value of " + str(target) + " is " + str(bin(target)[2:])



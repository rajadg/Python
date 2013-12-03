

# compute squares the old fashioned way
numbers = range(1,10)
squares = []
for num in numbers :
    if num % 2 == 0 :
        squares.append(num*num)
print squares
    
# square printing using list comprehension concept
squares = [i*i for i in range(1,10) if i % 2 ==0]
print squares

# using lambda
sq_cb_sum = lambda x: x**2 + (x+1)**3
squares_cube_sum = [sq_cb_sum(i) for i in range(1,10) if i % 2 ==0]
print squares_cube_sum


# function with multiple returns
def fun(x) :
    return x**2, (x+1)**3

fun2 = lambda x: (x**2, (x+1)**3)

squares_cube_sum = [fun2(i) for i in range(1,10) if i % 2 ==0]
print squares_cube_sum





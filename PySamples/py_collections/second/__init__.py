def test(a, b):
    print a + b

# basic function call    
test(10, 11)

# arguments as single array
par = [4,5]
test(*par)

# named arguments
test(a=10, b=25)

# using tuple as param
par = (11, 86)
test(*par)

data = { 'a' : 10, 'b':18 }
test(**data)

# call same function with string args
test("gopala ", "krishanan")




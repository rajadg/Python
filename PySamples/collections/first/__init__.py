
# this is an array (we call it list)
list_int = [1, 22, 3.5, 43, 5, 61, 7, "bindu", "gopal", "madhu"]
list_range = range(0,10)
print "list :" + str(list_int)
for i in list_range :
    print "list_int[" + str(i) + "] = " + str(list_int[i])

list_int.append("sridhar")
list_int.insert(0, "fanish")
list_int.remove(7)
print "new list: " + str(list_int)

# this is a dynamic structure (we call it tuple)
tuple = ("ramesh", 18, "bangalore", [10, 20, 30])
print "tuple :" + str(tuple)

print "first item in tuple : " + tuple[0]

# this is dictionary
employee = { "name": "ramesh", 
            "skill-level" : 10, 
            "city": "tuticorin" , 
            "addr" : ("SSDI", "ITPL", "bangalore", 56066)}


print "employee : " + str(employee)
print "city is " + employee["city"]

employee["lang"] = "java"
employee["city"] = None
for key in employee.keys() :
    print key + "= " + str(employee[key])


 
    
    
    
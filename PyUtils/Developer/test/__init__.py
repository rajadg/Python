
from Developer.JsonSerializer import JsonSerializer

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
class Rectangle:
    def __init__(self, top_left, bottom_right):
        self.top_left = top_left
        self.bottom_right = bottom_right
        

class myClass:
    def __init__(self):
        self.a = 10
        self.b = "20"
        self.c = [1,2,3,4,5]
        self.d = (10,20,30,40)
        self.data = {"name" : "ds", "lang" : "python", "priority": 11}
        self.loc = Point(11,12)
        self.rect = Rectangle(Point(0,0), Point(20,20))
        
myObj = myClass()
indent_string = "    "
serializer = JsonSerializer(indent_string, True, True)

print "test case for " + str(serializer.__class__)

print "instance myObj in json format  method(JsonSerializer.var_to_json):"
print "var jsonData = { " + serializer.var_to_json("myClass", myObj, 3) + "\n" + indent_string + "};\n"

print "instance myObj in json format  method(JsonSerializer.var_to_js_object):"
print serializer.var_to_js_object("myClass", myObj, 3) + "\n"

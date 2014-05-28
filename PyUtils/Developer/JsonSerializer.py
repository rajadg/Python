'''
Created on Nov 29, 2013

@author: dgraja
'''

class JsonSerializer(object):
    '''
    Reflection class is used for describing an Object
    
    
    '''

    '''
        Reflection Constructor
    '''
    def __init__(self, space, use_new_line, show_class_name):
        '''
        Constructor
        '''
        self.space = space
        self.use_new_line = use_new_line
        self.show_class_name = show_class_name
        self.quote = "'"
        self.recursion = 0
        pass
    # end of constructor

    '''
        Gets the type of the Object
    '''
    def object_meta_data(self, target):
        '''
        Provide the meta-data on object like type, name, fully-qualified-name
        '''
        obj_type = "class"
        short_name = ""
        full_name = ""
        if (target == None or target.__class__ == None) :
            obj_type = "null"
        elif (str(type(target.__class__)) == "<type 'classobj'>") or hasattr(target, '__dict__'):
            obj_type = "class"
            short_name = target.__class__.__name__
            full_name = str(target.__class__)
            pass
        else :
            obj_type = str(target.__class__.__name__)
        return obj_type, short_name, full_name
    # end of object_meta_data method
    
    def var_to_json_ex(self, name, target, indent):
        self.recursion = 0
        return self.var_to_json(name, target, indent)
    
    '''
        Convert a variable to JSON Representation
    '''
    def var_to_json(self, name, target, indent):
        level = self.recursion
        self.recursion = self.recursion + 1
        try:
            if self.recursion > 16 :
                raise Exception("complicated data")
            # invoke the any_to_json
            var_json_result = self.any_to_json(target, indent)
            # assemble the data
            if (None == name) :
                # expansion of object as part of list or tuple or dictionary
                var_json_result = var_json_result
            else:
                # expansion of object which is a member or a variable
                var_json_result = self.quote + str(name) + self.quote + " : " + str(var_json_result)
            return var_json_result
        finally:
            self.recursion = self.recursion - 1
    # end of var_to_json method

    '''
        Convert a variable to JSON Representation
    '''
    def var_to_js_object(self, name, target, indent):
        # invoke the any_to_json
        var_json_result = self.any_to_json(target, indent)
        # assemble the data
        if (None == name) :
            # expansion of object as part of list or tuple or dictionary
            var_json_result = var_json_result
        else:
            # expansion of object which is a member or a variable
            var_json_result = "var " + name + " = " + var_json_result + ";"
        return var_json_result
    # end of var_to_json method

    ''' 
        Convert any object to a JSON String
    '''
    def any_to_json(self, target, indent):
        obj_type, short_name, full_name = self.object_meta_data(target)
        generic_json_result = ""
        if (obj_type == 'null') :
            generic_json_result = 'null'
        elif (obj_type == 'int') :
            generic_json_result = str(target)
        elif (obj_type == 'float') :
            generic_json_result = str(target)
        elif (obj_type == 'long') :
            generic_json_result = str(target)
        elif (obj_type == 'bool') :
            generic_json_result = str(target)
        elif (obj_type == 'unicode') :
            generic_json_result = "{ " + self.quote + "unicode" + self.quote + " : " + self.quote + str(target) + self.quote + "}"
        elif (obj_type == 'str') :
            generic_json_result = self.quote + str(target) + self.quote
        elif (obj_type == 'list') :
            generic_json_result = self.list_to_json(target, indent)
        elif (obj_type == 'tuple') :
            generic_json_result = "{" + self.quote + "tuple" + self.quote + " : " + self.list_to_json(target, indent) + "}"
        elif (obj_type == 'dict') :
            generic_json_result = self.dict_to_json(target, indent, short_name, full_name)
        elif (obj_type == 'class') :
            generic_json_result = self.class_to_json(target, indent, short_name, full_name)
        else:
            generic_json_result = self.quote + obj_type + self.quote + ":" + str(target)

        # remove new-line chars if the data is too small
        short_string = generic_json_result.replace("\n", " ")
        # trim double spaces to single space
        while short_string.find("  ") >= 0 :
            short_string = short_string.replace("  ", " ")
            pass
        
        # if the short_string can accumulate in one line, use short_string
        if (len(short_string) < 80) :
            generic_json_result = short_string;
            pass 
        
        # return the data
        return generic_json_result

    # end of any_to_json method
    
    '''
        Make the Spaces for the given Indent
    '''
    def generate_spaces(self, indent):
        result = " "
        if (self.use_new_line == True) :
            result += "\n"
            if (indent >= 0) :
                for count in xrange(1, indent) :
                    result += self.space
                    pass
                pass
            pass
        return result
    # end of generate_spaces method

    '''
        Serialize the list to JSON format
    '''
    def list_to_json(self, target, indent):
        result = ""
        # ignore empty objects
        if (None == target or target.__class__ == None):
            return "null"
        class_name = str(target.__class__.__name__)
        # ignore anything not a list or tuple
        if (class_name != "list" and class_name != "tuple"):
            return result
        
        # expand the target object as a list
        result = "["
        for index in xrange(0, len(target)) :
            if (len(result) > 1) :
                result = result + ","
            result = result + self.generate_spaces(indent + 1) + self.any_to_json(target[index], indent + 1)
            pass
        
        result = result + self.generate_spaces(indent) + "]"
        return result
    # end of list_to_json method

    '''
        Serialize the given object as a JSON String
        
        This method is for serializing an object of a class
    '''
    def class_to_json(self, target, indent, short_name, full_name):
        result = "{"
        # ignore empty objects
        if None == target or target.__class__ == None or \
           (str(type(target.__class__)) != "<type 'classobj'>" and not hasattr(target, '__dict__')):
            return "null"

        if (self.show_class_name) :
            result = result + self.generate_spaces(indent + 1) + self.quote + "class" + self.quote + " : " 
            result = result + self.quote + short_name + "@" + full_name + self.quote
            pass
        
        # iterate through all the members of the class        
        for name, value in vars(target).iteritems():
            if (len(result) > 1) :
                result += ","
                pass
            if name[:4] == "____" and name[-4:] == "____" :
                continue
            data = self.var_to_json(name, value, indent + 1)
            result += self.generate_spaces(indent + 1) + data
            pass
        
        result += self.generate_spaces(indent) + "}"
        return result
    # end of class_to_json method
        


    '''
        Serialize the given dictionary as a JSON String
        
        This method is for serializing a dictionary
    '''
    def dict_to_json(self, target, indent, short_name, full_name):
        result = "{"
        # ignore empty objects
        if (None == target or target.__class__ == None or str(target.__class__.__name__) != "dict"):
            return "null"

#         if (self.show_class_name) :
#             result = self.generate_spaces(indent+1) + self.quote + "dictionary" + self.quote + " : " 
#             result = result + self.quote + short_name + "@" + full_name + self.quote
#             pass
        
        # iterate through all the members of the class        
        for key in target.keys():
            if (len(result) > 1) :
                result += ","
                pass
            value = target[key]
            data = self.var_to_json(key, value, indent + 1)
            result += self.generate_spaces(indent + 1) + data
            pass
        
        result += self.generate_spaces(indent) + "}"
        return result
    # end of dict_to_json method
        
    pass  # end of class


        

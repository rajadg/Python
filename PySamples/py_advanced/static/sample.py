
class static_sample :
    _static_counter = 1
    
    def __init__ (self):
        self._instance_id = static_sample._static_counter
        static_sample._static_counter += 1
    
    def print_id(self):
        print "static_sample instance id is " + str(self._instance_id)
        
    @staticmethod
    def update_counter(newValue):
        static_sample._static_counter = newValue
        
    @staticmethod
    def reset_counter():
        static_sample._static_counter = 1
        
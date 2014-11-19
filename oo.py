class ClassName(object):
    def __init__(self, additional, arguments):
        self.attr = additional + arguments
        self._val = None
        
    def method(self):
        print self.attr
        
    @property
    def prop(self):
        return self.attr * 2
    
    def val_getter(self):
        return self._val
    
    def val_setter(self, value):
        self._val = value
    
class DerivedClass(ClassName):
    def __init__(self, arg1, arg2):
        super(DerivedClass, self).__init__(arg1, arg2)
    

obj = ClassName(1, 2)
obj.method()

new_obj = DerivedClass(2 ,4)

print obj.prop
print obj._val

print new_obj.prop
print new_obj._val

print ClassName
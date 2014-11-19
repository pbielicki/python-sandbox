
class ClassName(object): # deriving from object means "use new-style class"
    class_level_attribute = "something"
    # no constructor !
    # we have an initializer instead
    def __init__(self, additional, arguments):
        self.attribute = additional + arguments
        self._val = None

    def method(self):
        print self.attribute

    @property
    def prop(self):
        return self.attribute *2

    def val_getter(self):
        return self._val
    def val_setter(self, value):
        if value is not None:
            self._val = value
        else:
            raise ValueError(value)
    val = property(val_getter, val_setter)

class DerivedClass(ClassName):
    def __init__(self, arg1, arg2):
        super(DerivedClass, self).__init__(v)
        # alternative way, with single inheritance:
        # ClassName.__init__(self, arg1, arg2)

my_object = ClassName(1, 2)
my_object.method()
print my_object.attribute # read access
my_object.attribute = 42 # write access
my_object.foobar = 33

print my_object.prop
#error:
# my_object.prop = 22

print my_object.val
my_object.val = 11
try:
    my_object.val = None
except ValueError:
    print 'test OK'

    

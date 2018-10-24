
class Child:

    def get_config_value(self):
        print("Child config value")
        return

class Parent:
    def __new__(cls, args=None):
        print("Creating Instance")
        instance = Child() 
        print(args)
        return instance

    def __init__(self, input_1=None):
        print("Parent input is called....")
        obj = Child()
        print(obj.__class__.__name__)
        obj.get_config_value()
        return obj

    def get_config_value(self):
        print("Parent config value")



t = Parent("test")
print(t.__class__.__name__)
t.get_config_value()
tt = Parent()

class SingleObj(object):
    _instance = None
    def __init__(self):
        print("Calling Constructor")

    def __new__(cls):
        if cls._instance is None:
            print("Creating New instance")
            cls._instance = super(SingleObj, cls).__new__(cls)
        return cls._instance

obj_1 = SingleObj()
obj_2 = SingleObj()

print(obj_1 == obj_2)
print(obj_1, obj_2)

class SingletonClass(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonClass, cls).__new__(cls)
        return cls.instance

singleton = SingletonClass()
new_singleton = SingletonClass()

print(singleton is new_singleton)

singleton.singl_variable = "Singleton Variable"
print(new_singleton.singl_variable)

print(singleton, new_singleton)

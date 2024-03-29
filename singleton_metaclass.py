#https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class MyClass:
    __metaclass__ = Singleton
    def __init__(self):
        self.name = "sheetal"

    def printName(self):
        return self.name

    def changeName(self, name):
        self.name = name


t1 = MyClass()
print(t1.printName())

t2 = MyClass()
print(t2.printName())

print(id(t1))
print(id(t2))

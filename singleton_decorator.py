def singleton(class_):
    print('steps')
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        print('steps')
        return instances[class_]
    return getinstance

@singleton
class MyClass:
    pass

obj1 = MyClass()
obj2 = MyClass()
print(id(obj2), id(obj1))
print(obj1 is obj2)
print(obj1 == obj2)

#https://dbader.org/blog/meaning-of-underscores-in-python
class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 23

class ExtendedTest(Test):
    def __init__(self):
        super().__init__()
        self.foo = 'overridden'
        self._bar = 'overridden'
        self.__baz = 'overridden'

t2 = ExtendedTest()
print(t2.foo)
print(t2._bar)
print(t2._ExtendedTest__baz)
print(t2._Test__baz) # Variable '_Test_baz' is a private variable of class Test().
print(t2.__dict__)

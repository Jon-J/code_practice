class Test:
    def __init__(self):
        self.a = 1
        self.b = 2

    def printValueA(self):
        return print(self.a)

    def printValueB(self):
        return print(self.b)

test = Test()
test.printValueA()
test.printValueB()

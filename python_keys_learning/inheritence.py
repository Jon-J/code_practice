class A:
    def test(self):
        print('Print Class A - {}'.format(self.var1))
        return

class B:
    def __init__():
        self.__var3 = 'Var _B__3'

    def test_2(self):
        print('Print Class B - {}'.format(self.var1))

    def test_3(self):
        print('Print Class B - {}'.format(self._var2))

    def test_4(self):
        print('Print Class B - {}'.format(self.__var3))

class C(A,B):
    def __init__(self):
        self.var1 = 'Var 1'
        self._var2 = 'Var 2'
        self.__var3 = 'Var 3'
        super(B).__init__()

obj = C()
obj.test()
obj.test_2()
obj.test_3()
obj.test_4()

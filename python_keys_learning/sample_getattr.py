#https://blog.rmotr.com/python-magic-methods-and-getattr-75cf896b3f88

class Dummy(object):
    def __getattr__(self, attr):
        return attr.upper()
d = Dummy()
var1 = d.does_not_exist # 'DOES_NOT_EXIST'
var2 = d.what_about_this_one  # 'WHAT_ABOUT_THIS_ONE'
print(var1)
print(var2)

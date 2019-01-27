#http://farmdev.com/src/secrets/magicmethod/index.html
class Test(object):
    def __init__(self):
        self.a = 'a'
        self.b = 'b'

    def __getattr__(self, name):
        return 123456

t = Test()
print('object variables: %r' % t.__dict__.keys())
print(t.a)
print(t.b)
print(t.c)
print(getattr(t, 'd'))
print(hasattr(t, 'x'))

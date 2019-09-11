class Test:
    def __init__(self):
        self.a = 2

    def __getattr__(self, attr):
        return "{} attribute does not exists".format(attr)

d = Test()
print(d.does_not_exists)

print(d.a)

d.b = 'sid'

print(d.b)

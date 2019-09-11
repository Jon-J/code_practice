class Length:
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return "String - Length(%s) " % (len(self.data))
    def __repr__(self):
        return "Length(%s) " % (len(self.data))

t = Length("test")
print(t)
print(repr(t))

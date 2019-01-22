class Person(object):
  def __init__(self):
    self._name = ';'
  @property
  def name(self):
    print("Getting: %s" % self._name)
    return self._name
  @name.setter
  def name(self, value):
    print("Setting: %s" % value)
    self._name = value.title()
  @name.deleter
  def name(self):
    print("Deleting: %s" % self._name)
    del self._name

obj = Person
print(obj.name)
obj.name = "Sheetal"
print(obj.name)
del(obj.name)
#print(obj.name)

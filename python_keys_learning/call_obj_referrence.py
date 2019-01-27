a = 6667777
print(id(a))

def test(b):
  print(id(b))
  b = 7899987
  print(id(b))

test(a)

strs = ['ccc', 'aaaa', 'd', 'bb']
print(sorted(strs, key=len))  ## ['d', 'bb', 'ccc', 'aaaa']

def test():
    a = 20
    b = 10
    return a,b

res1, res2 = test()
print(res1, res2)

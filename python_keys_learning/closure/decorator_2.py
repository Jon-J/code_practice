def gen_power(exp):
    def power(func):
        def inner_func(*args):
            base = func(*args)
            return base ** exp
        return inner_func
    return power

@gen_power(2)
def raise_two(n):
    return n

@gen_power(3)
def raise_three(m):
    return m

print(raise_two(3))  #- 9
print(raise_three(2)) #- 8

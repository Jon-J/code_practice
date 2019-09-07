a_var = 'global variable'

def a_func():
    print(a_var, '[ a_var inside a_func() ]')

a_func()
print(a_var, '[ a_var outside a_func() ]')

print('***************************************')
a_var = 'global value'

def a_func():
    a_var = 'local value'
    print(a_var, '[ a_var inside a_func() ]')

a_func()
print(a_var, '[ a_var outside a_func() ]')
print('***************************************')

a_var = 'global value'

def a_func():
    global a_var
    a_var = 'local value'
    print(a_var, '[ a_var inside a_func() ]')

print(a_var, '[ a_var outside a_func() ]')
a_func()
print(a_var, '[ a_var outside a_func() ]')
print('***************************************')

a_var = 'global value'

def outer():
    a_var = 'enclosed value'

    def inner():
        a_var = 'local value'
        print(a_var)

    inner()

outer()
print('***************************************')

a_var = 'global variable'

def len(in_var):
    print('called my len() function')
    l = 0
    for i in in_var:
        l += 1
    return l

def a_func(in_var):
    len_in_var = len(in_var)
    print('Input variable is of length', len_in_var)

a_func('Hello, World!')

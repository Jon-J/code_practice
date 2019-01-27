#https://sebastianraschka.com/Articles/2014_python_scope_and_namespaces.html
a_var = 'global value'

def outer():
       a_var = 'local value'
       print('outer before:', a_var)
       def inner():
           #a_var = 'inner value'
           nonlocal a_var
           print('in inner():', a_var)
       inner()
       print("outer after:", a_var)
outer()

def outer_2():
       a_var = 'local value'
       print('outer_2 before:', a_var)
       def inner():
           nonlocal a_var
           a_var = 'inner value'
           print('in inner():', a_var)
       inner()
       print("outer_2 after:", a_var)
outer_2()

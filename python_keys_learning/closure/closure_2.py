def increament(num):
    def inner_func():
        return num + 1
    return inner_func()

print(increament(1))

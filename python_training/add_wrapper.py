
def outer():
    def inner(fn, input_list):
        val_a = input_list.pop(0)
        for val_b in input_list:
            print("Sum of a = {} & b = {} is: ".format(val_a, val_b))
            val_a = fn(val_a, val_b)
            print(val_a)
        return val_a
    return inner

def add(X, Y):
    return X + Y

test_sum = outer()
result = test_sum(add, [1,2,3,4])
print("Final output = ", result)

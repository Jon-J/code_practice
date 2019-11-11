from stack_impl import Stack

def find_span(input_val):
    stack = Stack()
    result = [None] * len(input_val)

    for i in range(0, len(input_val)):
        while not stack.is_empty() and input_val[i] > input_val[stack.peek()]:
            stack.pop()

        if stack.is_empty():
            p = -1
        else:
            p = stack.peek()

        result[i] = i - p

        stack.push(i)
    return result

a = [6, 3, 4, 5, 2]
print(find_span(a))
a = [ 10, 4, 5, 90, 120, 80] 
print(find_span(a))

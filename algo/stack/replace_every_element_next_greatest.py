from stack_impl import Stack

def next_greater(arr):
    elem = 0
    next_val = 0 
    
    stack = Stack()
    stack.push(arr[0])
    res = []
    for i in range(0, len(arr)):
        next_val = arr[i]
        if not stack.is_empty():
            elem = stack.pop()
            while elem < next_val:
                res.append(next_val)
                if stack.is_empty():
                    break
                elem = stack.pop()

            if elem > next_val:
                stack.push(elem)

        stack.push(next_val)


    while not stack.is_empty():
        elem = stack.pop()

        res.append(-1)

    print(res)

a = [16, 17, 4, 3, 5, 2]
next_greater(a)
next_greater([6, 12, 4, 1, 2, 111, 2, 2, 10])
next_greater([11, 13, 21, 3, 4, 2])
next_greater([4, 5, 2, 25])

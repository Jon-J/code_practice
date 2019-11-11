from stack_impl import Stack

def reverse_stack(curr_stack, new_stack):
    if curr_stack.is_empty():
        return

    new_stack.push(curr_stack.pop())
    reverse_stack(curr_stack, new_stack)
    return

s = Stack()
new_stack = Stack()

s.push(1)
s.push(2)
s.push(3)
print("curr stack")
print(s)
reverse_stack(s, new_stack)
print("new stack")
print(new_stack)
#print(s.pop())
#print(s.pop())
#print(s.pop())

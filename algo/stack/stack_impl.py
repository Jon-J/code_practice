class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)
    
    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def __repr__(self):
        return "Stack - {}".format(self.stack)

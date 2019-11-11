from stack_impl import Stack

class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enque(self, data):
        self.s1.push(data)

    def dequeue(self):
        if self.s2.is_empty():
            if not self.s1.is_empty():
                while not self.s1.is_empty():
                    self.s2.push(self.s1.pop())

            else:
                return
        return self.s2.pop()

q = Queue()

q.enque(1)
q.enque(2)
q.enque(3)
q.enque(4)
q.enque(5)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

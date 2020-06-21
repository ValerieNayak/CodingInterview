# Valerie Nayak
# 6/20/2020
# Question 3.4

from collections import deque

class MyQueue:
    def __init__(self, queue = []):
        self.primary = deque(queue)
        self.transfer = deque()

    def enqueue(self, item):
        self.primary.append(item)
    
    def dequeue(self):
        self.move(forward=True)
        popped = self.transfer.pop()
        self.move(forward=False)
        return popped
    
    def move(self, forward=True):
        if forward:
            from_stack = self.primary
            to_stack = self.transfer
        else:
            from_stack = self.transfer
            to_stack = self.primary
        while len(from_stack) > 0:
            to_stack.append(from_stack.pop())

    def display(self):
        print(self.primary)

raw = [1, 2, 3, 4]
q = MyQueue(queue=raw)
print(q.dequeue())
q.enqueue(5)
q.display()
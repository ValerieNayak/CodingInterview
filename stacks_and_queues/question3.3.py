# Valerie Nayak
# 6/18/2020
# Question 3.3

from collections import deque

class SetOfStacks:

    def __init__(self, capacity=3):
        self.stacks = deque()
        self.capacity = capacity
    
    def push(self, data):
        size = len(self.stacks)
        if size > 0 and len(self.stacks[size-1]) < self.capacity:
            self.stacks[size-1].append(data)
        else:
            new_stack = deque([data])
            self.stacks.append(new_stack)
    
    def pop(self):
        size = len(self.stacks)
        popped = self.stacks[size-1].pop()
        if len(self.stacks[size-1]) == 0:
            self.stacks.pop()
        return popped
    
    def display(self):
        for s in self.stacks:
            print(s)

stacks = SetOfStacks()
stacks.push(1)
stacks.push(2)
stacks.push(3)
stacks.push(4)
stacks.display()
print(stacks.pop())
print(stacks.pop())
stacks.display()
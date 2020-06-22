# Valerie Nayak
# 6/21/2020
# Question 3.2

from collections import deque

class Node:
    def __init__(self, d):  # constructor
        self.data = d
        self.next = None

class stack_min:
    def __init__(self):
        self.stack = deque()
        self.min = None
    
    def push(self, data):
        node = Node(data)
        node.next = self.min
        if self.min is None or data < self.min.data:
            self.min = node
        self.stack.append(node)
    
    def pop(self):
        popped = self.stack.pop()
        if popped == self.min:
            self.min = popped.next
        return popped
    
    def get_min(self):
        return self.min

    def display(self):
        print('stack:', end=' ')
        for node in self.stack:
            print(node.data, end=' ')
        print()

stack = stack_min()
stack.push(3)
stack.push(5)
print(stack.get_min().data)
stack.push(1)
stack.push(6)

stack.display()
stack.pop()
print(stack.get_min().data)
stack.pop()
print(stack.get_min().data)

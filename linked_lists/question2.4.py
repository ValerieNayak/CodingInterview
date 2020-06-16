# Valerie Nayak
# 6/15/2020
# Question 2.4

class Node:
    def __init__(self, d):  # constructor
        self.data = d
        self.next = None


class LinkedList:
    
    def __init__(self, h=None):  # constructor
        # head is variable containing head node
        self.head = h
    
    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        current = self.head
        while current.next is not None:     # current is pointer iterating through list
            current = current.next
        current.next = Node(data)
        return current.next
    
    def prepend(self, data):
        # insert at the beginning
        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head

    def delete_with_value(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
    
    def del_by_pointer(self, p1, p2):
        if p1 == self.head:
            self.head = p1.next
        else:
            p2.next = p1.next
    
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next
        print()

def partition(og_list, x):
    p = og_list.head
    less_list = LinkedList()
    greater_list = LinkedList()
    while p is not None:
        if p.data < x:
            middle = less_list.append(p.data)
        else:
            greater_list.append(p.data)
        p = p.next
    middle.next = greater_list.head
    return less_list

l_list = LinkedList(Node(3))
l_list.append(5)
l_list.append(8)
l_list.append(5)
l_list.append(10)
l_list.append(2)
l_list.append(1)
l_list.display()
parted = partition(l_list, 5) 
parted.display()
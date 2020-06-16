# Valerie Nayak
# 6/15/2020
# Question 2.3

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

def delete_middle(my_list, pointer):
    p2 = my_list.head
    while p2.next != pointer:
        p2 = p2.next
    my_list.del_by_pointer(pointer, p2)

print('test 1')
l_list = LinkedList(Node('a'))
l_list.append('b')
c_pointer = l_list.append('c')  # pointer that points to c
l_list.append('d')
l_list.append('e')
l_list.append('f')
l_list.display()

delete_middle(l_list, c_pointer)
l_list.display()
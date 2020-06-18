# Valerie Nayak
# 6/18/2020
# Question 2.6

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
    
    def append_node(self, node):
        if self.head is None:
            self.head = Node(data)
            return
        current = self.head
        while current.next is not None:     # current is pointer iterating through list
            current = current.next
        current.next = node
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

def is_palindrome(my_list):
    rev = LinkedList()  # reversed
    p = my_list.head
    while p is not None:
        rev.prepend(p.data)
        p = p.next
    return compare(my_list, rev)

def compare(l_list1, l_list2):
    p1 = l_list1.head
    p2 = l_list2.head
    while p1 is not None and p2 is not None:
        if p1.data != p2.data:
            return False
        p1 = p1.next
        p2 = p2.next
    if p1 != p2:
        return False
    return True

test1 = LinkedList(Node(3))
test1.append(1)
# test1.append(1)
test1.append(3)
test1.append(1)
test1.display()
print(is_palindrome(test1))
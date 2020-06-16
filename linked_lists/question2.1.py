# Valerie Nayak
# 6/15/2020
# Question 2.1

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

def remove_dups(my_list):
    elements = set()
    p1 = my_list.head
    p2 = None
    while p1 is not None:
        if p1.data in elements:
            my_list.del_by_pointer(p1, p2)
            p1 = p1.next
        else:
            elements.add(p1.data)
            p2 = p1
            p1 = p1.next
    return my_list

print('test 1')
test_node = Node(1)
l_list = LinkedList(test_node)
l_list.append(2)
l_list.append(2)
l_list.append(3)
l_list.append(4)
l_list.display()

remove_dups(l_list)
l_list.display()

print('\ntest 2')
l_list2 = LinkedList(Node(1))
l_list2.append(1)
l_list2.display()
remove_dups(l_list2)
l_list2.display()

print('\ntest 3')
l_list3 = LinkedList(Node(5))
l_list3.append(3)
l_list3.append(5)
l_list3.append(2)
l_list3.append(4)
l_list3.append(5)
l_list3.display()
remove_dups(l_list3)
l_list3.display()

print('\ntest 4')
l_list4 = LinkedList(Node(2))
l_list4.append(2)
l_list4.append(3)
l_list4.append(5)
l_list4.display()
remove_dups(l_list4)
l_list4.display()
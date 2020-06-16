# Valerie Nayak
# 6/15/2020
# Question 2.2

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

def k_to_last(my_list, k):
    length = count_nodes(my_list)
    index = length - k
    p_ind = 0
    p = my_list.head
    while p_ind < index:
        p = p.next
        p_ind += 1
    return p

def count_nodes(my_list):
    count = 0
    p = my_list.head
    while p is not None:
        count += 1
        p = p.next
    return count

l_list = LinkedList(Node('a'))
l_list.append('b')
l_list.append('c')
l_list.append('d')
l_list.append('e')
l_list.display()

my_data = k_to_last(l_list, 1).data
print('data', my_data)

length = count_nodes(l_list)
print('length', length)

my_data = k_to_last(l_list, 5).data
print('data', my_data)

my_data = k_to_last(l_list, 3).data
print('data', my_data)
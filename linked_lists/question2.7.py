# Valerie Nayak
# 6/16/2020
# Question 2.7

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

def intersection(list1, list2):
    p = list1.head
    nodes = set()
    while p is not None:
        nodes.add(p)
        p = p.next
    p = list2.head
    while p is not None:
        if p in nodes:
            return p
        p = p.next
    return None

inp1 = LinkedList(Node('a'))
inp1.append('b')
my_node = inp1.append('c')
inp1.append('d')
inp2 = LinkedList(my_node)
# inp2 = LinkedList(Node('c'))
inp2.append('e')
inp2.append('f')
print('list 1:', end=' ')
inp1.display()
print('list 2:', end=' ')
inp2.display()

inter = intersection(inp1, inp2)
if inter is not None:
    print('intersect:', inter.data)
else:
    print('no intersect')
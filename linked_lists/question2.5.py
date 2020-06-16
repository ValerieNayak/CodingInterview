# Valerie Nayak
# 6/16/2020
# Question 2.5

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

def sum_lists(input1, input2):
    p1 = input1.head
    p2 = input2.head
    output = LinkedList()
    carry = 0
    temp_sum = 0
    while p1 is not None or p2 is not None or carry != 0:
        if p1 is not None:
            temp_sum += p1.data
            p1 = p1.next
        if p2 is not None:
            temp_sum += p2.data
            p2 = p2.next
        temp_sum += carry
        digit = temp_sum % 10
        output.append(digit)
        carry = temp_sum // 10
        temp_sum = 0
    return output

inp1 = LinkedList(Node(7))
inp1.append(1)
inp1.append(6)
inp2 = LinkedList(Node(5))
inp2.append(9)
inp2.append(2)
my_sum = sum_lists(inp1, inp2)
my_sum.display()

inp3 = LinkedList(Node(9))
inp3.append(1)
inp3.append(3)
inp4 = LinkedList(Node(9))
inp4.append(1)
my_sum2 = sum_lists(inp3, inp4)
my_sum2.display()

inp5 = LinkedList(Node(9))
inp5.append(9)
inp5.append(9)
inp6 = LinkedList(Node(1))
my_sum3 = sum_lists(inp5, inp6)
my_sum3.display()
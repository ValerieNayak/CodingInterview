# Valerie Nayak
# 6/22/2020
# Question 4.3

class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

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

def list_of_depths(root):
    depth_lists = []

    def depth_helper(node, depth):
        if node is not None:
            if len(depth_lists) <= depth:
                linked_list = LinkedList(Node(node))
                depth_lists.append(linked_list)
            else:
                depth_lists[depth].append(node)
            depth_helper(node.left, depth + 1)
            depth_helper(node.right, depth + 1)

    depth_helper(root, 0)
    return depth_lists

node_a = TreeNode('a')
node_b = TreeNode('b')
node_c = TreeNode('c')
node_d = TreeNode('d')
node_e = TreeNode('e')
node_f = TreeNode('f')
node_g = TreeNode('g')
node_a.left = node_b
node_a.right = node_c
node_b.left = node_d
node_b.right = node_e
node_c.left = node_f
node_d.left = node_g

list_depths = list_of_depths(node_a)
for height, l_list in enumerate(list_depths):
    print('height', height, end=' ')
    l_list.display()
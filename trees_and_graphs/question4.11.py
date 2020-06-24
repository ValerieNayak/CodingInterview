# Valerie Nayak
# 6/24/2020
# Question 4.11

import random

class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, root=None):
        self.root = None
        self.nodes = []

    def insert(self, value):
        new_node = TreeNode(value)
        self.nodes.append(new_node)
        
        if self.root is None:
            self.root = new_node
            return new_node

        p1 = self.root
        p2 = None
        left = False
        while p1 is not None:
            p2 = p1
            if value <= p1.data:
                p1 = p1.left
                left = True
            else:
                p1 = p1.right
                left = False
        if left:
            p2.left = new_node
        else:
            p2.right = new_node
        return new_node

    def get_random(self):
        rand_index = random.randint(0, len(self.nodes) - 1)
        return self.nodes[rand_index]

def test1():
    my_root = TreeNode(8)
    tree = BinarySearchTree(my_root)
    tree.insert(4)
    tree.insert(10)
    tree.insert(2)
    tree.insert(6)
    tree.insert(20)
    for node in tree.nodes:
        print(node.data, end=' ')
    print()

    print(tree.get_random().data)

test1()
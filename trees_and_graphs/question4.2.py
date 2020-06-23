# Valerie Nayak
# 6/22/2020
# Question 4.2

class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

def make_search_tree(elements):
    if len(elements) == 0:
        return None
    center = len(elements)//2
    print('current', elements[center])
    print('elements', elements)
    root = TreeNode(elements[center])
    root.left = make_search_tree(elements[:center])
    root.right = make_search_tree(elements[center + 1:])
    return root

def preorder_traversal(node):
    if node is not None:
        print(node.data, end = ' ')
        preorder_traversal(node.left)
        preorder_traversal(node.right)

def show_tree(node):
    if node is not None:
        print('data', node.data)
        if node.left is not None:
            print('left child', node.left.data)
        if node.right is not None:
            print('right child', node.right.data)
        print()
        show_tree(node.left)
        show_tree(node.right)

elems = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_root = make_search_tree(elems)
preorder_traversal(my_root)
print('\nshow tree')
show_tree(my_root)
# Valerie Nayak
# 6/24/2020
# Question 4.8

class TreeNode:
    def __init__(self, data=None, parent=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent

def first_common(node_a, node_b):
    height_a = get_height(node_a)
    height_b = get_height(node_b)
    if height_a >= height_b:
        p1 = node_a
        p2 = node_b
    else:
        p1 = node_b
        p2 = node_a
    difference = abs(height_a - height_b)
    for i in range(difference):
        p1 = p1.parent
    while p1 != p2:
        p1 = p1.parent
        p2 = p2.parent
    return p1

def get_height(node):
    pointer = node
    height = 0
    while pointer.parent is not None:
        height += 1
        pointer = pointer.parent
    return height

def test1():
    node8 = TreeNode(data=8)
    node4 = TreeNode(data=4, parent=node8)
    node10 = TreeNode(10, node8)
    node2 = TreeNode(2, node4)
    node1 = TreeNode(1, node2)
    node3 = TreeNode(3, node2)
    node6 = TreeNode(6, node4)
    node15 = TreeNode(15, node10)
    node20 = TreeNode(20, node10)

    node8.left = node4
    node8.right = node10
    node4.left = node2
    node4.right = node6
    node2.left = node1
    node2.right = node3
    node10.left = node15
    node10.right = node20

    common = first_common(node1, node6)
    return common.data

print(test1())
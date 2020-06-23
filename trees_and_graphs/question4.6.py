# Valerie Nayak
# 6/23/2020
# Question 4.6

class TreeNode:
    def __init__(self, data=None, parent=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent

def successor(node):
    pointer = node
    if pointer.right is not None:
        pointer = pointer.right
        while pointer.left is not None:
            pointer = pointer.left
        return pointer
    while pointer.parent is not None:
        pointer = pointer.parent
        if is_left(node, pointer):
            return pointer
    return None

traversals = dict()
def is_left(node, pointer):
    # check if node is left of pointer
    global traversals
    if pointer.left in traversals:
        left_children = traversals[pointer.left]
    else:
        left_children = preorder(pointer.left)
        traversals[pointer.left] = left_children
    if node in left_children:
        return True
    return False

def preorder(root):
    global traversals
    my_nodes = set()

    def helper(node):
        if node is not None:
            if node in traversals:
                my_nodes.update(traversals[node])
            else:
                my_nodes.add(node)
                helper(node.left)
                helper(node.right)
    
    helper(root)
    return my_nodes

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

    return successor(node3)

print(test1().data)

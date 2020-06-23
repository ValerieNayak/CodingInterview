# Valerie Nayak
# 6/23/2020
# Question 4.5

class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

def validate_bst(node):
    if node is None:
        return set()
    if node.left is None and node.right is None:
        return {node.data}
    left_validate = validate_bst(node.left)
    right_validate = validate_bst(node.right)
    if left_validate is False or right_validate is False:
        return False
    for num in left_validate:
        if num > node.data:
            return False
    for num in right_validate:
        if num <= node.data:
            return False
    nums = left_validate.union(right_validate)
    nums.add(node.data)
    return nums

def test1():
    n10 = TreeNode(10)
    n7 = TreeNode(7)
    n7b = TreeNode(7)
    n8 = TreeNode(8)
    n5 = TreeNode(5)
    n13 = TreeNode(13)
    n11 = TreeNode(11)
    n15 = TreeNode(15)

    n10.left = n7
    n10.right = n13
    n7.left = n7b
    n7.right = n8
    n7b.left = n5
    n13.left = n11
    n13.right = n15

    return validate_bst(n10)

def test2():
    n10 = TreeNode(10)
    n7 = TreeNode(7)
    n5 = TreeNode(5)
    n11 = TreeNode(11)
    n13 = TreeNode(13)
    n12 = TreeNode(12)
    n15 = TreeNode(15)

    n10.left = n7
    n10.right = n13
    n7.left = n5
    n7.right = n11
    n13.left = n12
    n13.right = n15

    return validate_bst(n10)

print(test2())
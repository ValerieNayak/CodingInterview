# Valerie Nayak
# 6/24/2020
# Question 4.10

# textbook solution (better solution): preorder traversal with Xs for null nodes. Compare substrings

from collections import deque

class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

def check_subtree(t1, t2):
    to_visit = deque()
    to_visit.append(t1)
    while len(to_visit) > 0:
        current = to_visit.popleft()
        if current == t2:
            return True
        if current.left is not None:
            to_visit.append(current.left)
        if current.right is not None:
            to_visit.append(current.right)
    return False

def test1():
    # this test should return True
    n3 = TreeNode(3)
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n4 = TreeNode(4)
    n8 = TreeNode(8)

    n3.left = n1
    n3.right = n2
    n1.left = n5
    n1.right = n6
    n5.left = n4
    n5.right = n8

    check = check_subtree(n3, n5)
    return check

def test2():
    # this one should return False
    n3 = TreeNode(3)
    n2 = TreeNode(2)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    
    n3.left = n2
    n3.right = n4

    check = check_subtree(n3, n5)
    return check

print(test2())

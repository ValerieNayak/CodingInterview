# Valerie Nayak
# 6/24/2020
# Question 4.12

import random

class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

def paths_with_sum(root, target_value):
    count_paths = [0]

    def path_helper(node, current_sum):
        # print('path helper called', current_sum)
        if node is not None:
            current_sum += node.data
            # print('current sum', current_sum)
            # print('count_paths', count_paths)
            if current_sum == target_value:
                count_paths[0] += 1
            path_helper(node.left, current_sum)
            path_helper(node.right, current_sum)
    
    path_helper(root, 0)
    return count_paths

def test1():
    na = TreeNode(1)
    nb = TreeNode(2)
    nc = TreeNode(3)
    nd = TreeNode(-1)
    ne = TreeNode(4)
    nf = TreeNode(5)
    ng = TreeNode(-1)

    na.left = nb
    na.right = nc
    nb.left = nd
    nb.right = ne
    nc.left = nf
    nc.right = ng

    count = paths_with_sum(na, 3)
    return count

print(test1())
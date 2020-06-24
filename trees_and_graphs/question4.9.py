# Valerie Nayak
# 6/24/2020
# Question 4.9

# UNFINISHED

import itertools

class TreeNode:
    def __init__(self, data=None, parent=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent

def list_of_depths(root):
    depth_lists = []

    def depth_helper(node, depth):
        if node is not None:
            if len(depth_lists) <= depth:
                current_list = [node]
                depth_lists.append(current_list)
            else:
                depth_lists[depth].append(node)
            depth_helper(node.left, depth + 1)
            depth_helper(node.right, depth + 1)

    depth_helper(root, 0)
    return depth_lists

def bst_sequences(dlists):
    perm_lists = []     # list of permutations
    for depth_list in dlists:
        perm_object = itertools.permutations(depth_list)
        plist = list(perm_object)
        perm_lists.append(plist)
        # print('plist', plist)
    sequences = []
    current_sequence = []
    index = 0
    count_sequences = 1
    for perms in perm_lists:
        count_sequences *= len(perms)
    while index < count_sequences:
        for perms in perm_lists:
            current_index = index % len(perms)
            current_sequence.extend(list(perms[current_index]))
        sequences.append(current_sequence)
        index += 1
        current_sequence = []
    return sequences

def display_sequences(seqs):
    for s in seqs:
        for node in s:
            print(node.data, end = ' ')
        print()    

def test1():
    node2 = TreeNode(2)
    node1 = TreeNode(1)
    node3 = TreeNode(3)

    node2.left = node1
    node2.right = node3

    dlists = list_of_depths(node2)
    sequences = bst_sequences(dlists)

    display_sequences(sequences)

def test2():
    n5 = TreeNode(5)
    n3 = TreeNode(3)
    n7 = TreeNode(7)
    n2 = TreeNode(2)
    n4 = TreeNode(4)
    n6 = TreeNode(6)

    n5.left = n3
    n5.right = n7
    n3.left = n2
    n3.right = n4
    # n7.left = n6

    dlists = list_of_depths(n5)
    sequences = bst_sequences(dlists)

    display_sequences(sequences)

# test1()
test2()
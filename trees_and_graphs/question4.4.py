# Valerie Nayak
# 6/22/2020
# Question 4.4

class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

def check_balanced(node, height):
    if node is not None:
        left_height = check_balanced(node.left, height+1)
        right_height = check_balanced(node.right, height+1)
        print('\nnode', node.data)
        # print('height', height)
        print('height', max(left_height, right_height))
        # print('left', left_height)
        # print('right', right_height)
        if left_height == False or right_height == False:
            return False
        elif abs(left_height - right_height) > 1:
            return False
        return max(left_height, right_height)
    else:
        return height-1

node_a = TreeNode('a')
node_b = TreeNode('b')
node_c = TreeNode('c')
node_d = TreeNode('d')
node_e = TreeNode('e')
node_f = TreeNode('f')
node_g = TreeNode('g')
node_h = TreeNode('h')
node_a.left = node_b
node_a.right = node_c
node_b.left = node_d
node_b.right = node_e
node_c.left = node_f
node_d.left = node_g
node_g.left = node_h

print('check balanced')
print(check_balanced(node_a, 0))
# Valerie Nayak
# 6/25/2020
# Question 4.1

from collections import deque

class GraphNode:
    def __init__(self, data=None):
        self.data = data
        self.children = []

def route(s, e):
    s_visited = set()
    s_queue = deque()
    e_visited = set()
    e_queue = deque()
    
    s_queue.append(s)
    e_queue.append(e)

    s_popped = False
    e_popped = False

    while len(s_queue) > 0 or len(e_queue) > 0:

        if len(s_queue) > 0:
            s_current = s_queue.popleft()
            s_visited.add(s_current)
            s_popped = True
        if len(e_queue) > 0:
            e_current = e_queue.popleft()
            e_visited.add(e_current)
            e_popped = True

        if len(s_visited.intersection(e_visited)) > 0:
            return True

        if s_popped:
            for child in s_current.children:
                if child not in s_visited:
                    s_queue.append(child)
        if e_popped:
            for child in e_current.children:
                if child not in e_visited:
                    e_queue.append(child)
    return False

def test1():
    s = GraphNode('s')
    a = GraphNode('a')
    b = GraphNode('b')
    c = GraphNode('c')
    d = GraphNode('d')
    f = GraphNode('f')
    e = GraphNode('e')
    g = GraphNode('g')
    
    s.children = [a, b, c]
    a.children = [s, d]
    b.children = [s, f]
    c.children = [s]
    d.children = [a, f]
    f.children = [d, b, e]
    e.children = [f]

    return route(s, e)

print(test1())
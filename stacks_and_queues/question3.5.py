# Valerie Nayak
# 6/20/2020
# Question 3.5

from collections import deque

def sort_stack(stack):
    processed = deque()
    temp = deque()
    while len(stack) > 0:
        # print()
        # print('processed', processed)
        current = stack.pop()
        # print('current', current)
        while len(processed) > 0 and processed[-1] < current:
            temp.append(processed.pop())
        # print('processed', processed)
        # print('temp', temp)
        processed.append(current)
        while len(temp) > 0:
            processed.append(temp.pop())
    stack = processed
    return stack

my_stack = deque([5, 7, 2, 3, 1, 8, 6, 4])
print(sort_stack(my_stack))
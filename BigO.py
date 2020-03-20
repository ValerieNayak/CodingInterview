# Valerie Nayak
# 3/20/2020
# Cracking the Coding Interview: Big O

#### Example 1
# O(N)
def foo(array):
    # arry is list of ints
    sum = 0
    product = 1
    for i in array: # O(N)
        sum += i
    for i in array: # O(N)
        product *= i
    print("sum :", sum, "product:", product)

### Example 2
# O(N^2)
def print_pairs(array):
    for i in array:
        for j in array:
            print(i, ",", j)
array = [1, 2, 3, 4]
# print_pairs(array)

### Example 3
# O(N^2)
def print_unordered_pairs(array):
    for i in range(0, len(array)):
        for j in range(i, len(array)):
            print(i, ",", j)
print_unordered_pairs(array)

### Example 4
def print_two_pairs(arrayA, arrayB):
    for i in arrayA:
        for j in arrayB:
            if i > j:
                print(i, j)
# O(ab)

### Example 5
# O(ab)

### Example 6
# O(N)

### Example 7
# all but the last one are O(N)

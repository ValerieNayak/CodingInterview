# Valerie Nayak
# 4/6/2020
# Cracking the Coding Interview, p. 90
# 1.7: Rotate Matrix

def rotate_clock(matrix):
    # rotate a 2d list 90 degrees clockwise
    # matrix is nxn
    reversed = matrix[::-1]
    rotated = []
    n = len(matrix)
    for i in range(n):
        rotated.append([])
    for row in reversed:
        for col_index, val in enumerate(row):
            rotated[col_index].append(val)
    return rotated

def display(matrix):
    for row in matrix:
        for val in row:
            temp_str = str(val).rjust(2, ' ')
            print(temp_str, end = ' ')
        print()


# my_mat = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
my_mat = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
display(my_mat)
rotated = rotate_clock(my_mat)
print()
display(rotated)

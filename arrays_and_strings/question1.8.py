# Valerie Nayak
# 4/6/2020
# Cracking the Coding Interview, p. 90
# 1.8: Zero Matrix
# THIS IS NOT WORKING YET

def zero_mat(matrix):
    for r_ind, row in enumerate(matrix):
        for c_ind, val in enumerate(row):
            if val == 0:
                for temp_col in range(len(row)):
                    matrix[r_ind][temp_col] = 0
                col = column(matrix, c_ind)
                for temp_row in range(len(col)):
                    matrix[temp_row][c_ind] = 0
    return matrix

def column(matrix, i):
    return [row[i] for row in matrix]

def display(matrix):
    for row in matrix:
        for val in row:
            temp_str = str(val).rjust(2, ' ')
            print(temp_str, end = ' ')
        print()

my_mat = [[1, 2, 0], [5, 7, 6], [1, 2, 3]]
display(my_mat)
print()
modified = zero_mat(my_mat)
display(modified)
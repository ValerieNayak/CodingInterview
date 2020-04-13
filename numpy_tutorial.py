# Valerie Nayak
# 4/9/2020
# Numpy Tutorial

import numpy as np
import time
import sys
import matplotlib.pyplot as plt

print("PART 1 - construct np array")
# a = np.array([1, 2, 3])
a = np.array([(1, 2, 3), (4, 5, 6)])
print(a)

print("\nPART 2 - np arrays use less memory than lists")
s = range(1000)
print(sys.getsizeof(5) * len(s))    # size of list in memory

d = np.arange(1000)
print(d.size * d.itemsize)  # size of np array in memory

print("\nPART 3 - np arrays are faster than lists")
size = 1000000
list1 = range(size)
list2 = range(size)
arr1 = np.arange(size)
arr2 = np.arange(size)
# compute sum of both arrays

start = time.time()
result = [(x, y) for x,y in zip(list1, list2)]
print('time to sum lists:', (time.time() - start) * 1000) # print time in milliseconds

start = time.time()
result = arr1 + arr2
print('time to sum arrays:', (time.time() - start) * 1000) # print time in milliseconds

print("\nPART 4 - array operations")
a = np.array([(1, 2, 3), (2, 3, 4)])
print('a dimensions:', a.ndim)
print('byte size of each element:', a.itemsize)
print('data type:', a.dtype)
print('size (num elements):', a.size)
print('shape:', a.shape)

print("\nPART 5 - reshape and slice arrays") 

a = np.array([(1, 2, 3, 4), (3, 4, 5, 6)])
print(a)
print("reshape")
a = a.reshape(4, 2)
print(a)

a = np.array([(1, 2, 3, 4), (3, 4, 5, 6), (7, 8, 9, 10)])
print('slicing and indexing')
print(a[0, 2])
print(a[0:2, 3]) # look at rows 0 and 1 and print the third index from each --> [4 6]

print("\nPART 6 - other numpy functions")
a = np.linspace(1, 3, 5) # return evenly spaced numbers over interval
# print 5 values between 1 and 3 inclusive
print(a)

a = np.array([1, 2, 3])
print('max:', a.max()) 
print('min:', a.min())
print('sum elements:', a.sum())

print("\nPART 7 - axes, square roots, stdevs")

print('rows are axis 1, cols are axis 0')
a = np.array([(1, 2, 3), (3, 4, 5)])
print(a)
col_sum = a.sum(axis=0) # find sum of each column (axis 0)
print('axis 0 (col) sum:', col_sum)
row_sum = a.sum(axis=1) # find sum of each row (axis 1)
print('axis 1 (row) sum:', row_sum)

square_root = np.sqrt(a)
print('\nsquare root of each element')
print(square_root)

stdev = np.std(a)
print('\nstandard deviation of array')
print(stdev)

print('\nPART 8 - add, subtract, multiply, divide')
# same a from previous section
print('these operations perform element-wise arithmetic')
b = np.array([(1, 2, 3), (3, 4, 5)])
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print('\nPART 9 - stacking and concatenation')
print('stacking is like concatenation for np arrays')
vert_stack = np.vstack((a, b))
print('vertical stack')
print(vert_stack)

horiz_stack = np.hstack((a, b))
print('horizontal stack')
print(horiz_stack)

print('\nconvert array a to single row')
print(a.ravel())

print('\nPART 10 - numpy special functions')
# imported matplotlib for this
print('uncomment these lines to see graph')
x = np.arange(0,3*np.pi, 0.1)
y = np.sin(x)
plt.plot(x, y)
# plt.show()

print('\nexponential functions')
ar = np.array([1, 2, 3])
exponents = np.exp(ar) # e raised to the power of value in array
print(exponents)

print('\nlogs')
nat_log = np.log(ar)
print('natural log')
print(nat_log)

print('log base 10')
log10 = np.log10(ar)
print(log10)
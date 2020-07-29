# Valerie Nayak
# 7/29/2020
# Quick Sort

# not complete yet

def quicksort(arr, left, right):
    print(arr)
    print('left', left)
    print('right', right)
    if left < right:
        arr, mid = partition(arr, left, right)
        print('mid', mid)
        arr = quicksort(arr, left, mid-1)
        arr = quicksort(arr, mid, right)
        return arr

def partition(arr, left, right):
    # print('pleft', left)
    # print('pright', right)
    ind1 = left
    ind2 = right
    part = arr[right]
    while ind1 < ind2:
        while arr[ind1] < part:
            ind1 += 1
        while arr[ind2] > part:
            ind2 -= 1
        if ind1 <= ind2:
            arr = swap(arr, ind1, ind2)
            ind1 += 1
            ind2 -= 1
        # print('arr', arr)
    print(ind1)
    return arr, ind1

def swap(arr, ind1, ind2):
    temp = arr[ind1]
    arr[ind1] = arr[ind2]
    arr[ind2] = temp
    return arr

a = [12, 11, 13, 5, 6, 7]
a = quicksort(a, 0, len(a)-1)
# a = [6, 5, 13, 11, 12, 7]
# a = quicksort(a, 2, 5)
print(a)
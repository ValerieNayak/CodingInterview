# Valerie Nayak
# 7/28/2020
# Merge Sort

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[: mid]
    right = arr[mid :]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    merged = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    if len(left) > 0:
        merged.extend(left)
    if len(right) > 0:
        merged.extend(right)
    return merged

a = [12, 11, 13, 5, 6, 7]
a = merge_sort(a)
print(a)
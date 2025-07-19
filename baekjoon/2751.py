# https://www.acmicpc.net/problem/2751


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    """
    split the array into two halves
    """
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    i = j = k = 0

    """
    merge left and right arrays
    """
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    """
    copy remaining elements from right or left array
    """
    if i == len(left):
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

    return arr


n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

arr = merge_sort(arr)

for data in arr:
    print(data)

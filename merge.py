arr = list(map(int, input().split()))

def merge_sort(arr):

    temp = []
    i, j = 0, 0

    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            temp.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            j += 1
    while i < len(left):
        temp.append(left[i])
        i += 1
    while j < len(right):
        temp.append(right[j])
        j += 1

    return temp

print(merge_sort(arr))
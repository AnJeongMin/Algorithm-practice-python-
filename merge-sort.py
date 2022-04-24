list = list(map(int, input().split()))

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left_child = merge_sort(left)
    right_child = merge_sort(right)
    return merge(left_child, right_child)

def merge(left, right):
    i, j = 0, 0
    result = []

    while(i < len(left)) and (j < len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    while(i < len(left)):
        result.append(left[i])
        i+=1

    while(j < len(right)):
        result.append(right[j])
        j+=1

    return result

print(merge_sort(list))

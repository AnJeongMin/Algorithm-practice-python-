def bisect_left_impl(arr, x):
    l, r = 0, len(arr)
    idx = len(arr)
    while l <= r:
        mid = (l+r)//2
        if x <= arr[mid]:
            idx = mid
            r = mid-1
        else:
            l = mid+1
    return idx

def bisect_right_impl(arr, x):
    l, r = 0, len(arr)
    idx = len(arr)
    while l <= r:
        mid = (l+r)//2
        if arr[mid] <= x:
            idx = mid
            l = mid+1
        else:
            r = mid-1
    return idx

arr = [1, 2, 3, 4, 5, 5, 6, 6, 6, 7, 7, 8]
tar = 6
print(bisect_left_impl(arr, tar))
print(bisect_right_impl(arr, tar))
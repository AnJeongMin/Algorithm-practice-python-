def binary_search_recur(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search_recur(arr, target, start, mid - 1)
    else:
        return binary_search_recur(arr, target, mid + 1, end)   
    
def binary_search_iter(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n, target = map(int, input().split())
arr = list(map(int, input().split()))
 
result = binary_search_iter(arr, target, 0, n - 1)

if result == None:
    print("Not exist")
else:
    print(str(result + 1) + "th")



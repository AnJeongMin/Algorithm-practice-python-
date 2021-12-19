from bisect import bisect_left, bisect_right

n, x = map(int, input().split())

arr = list(map(int, input().split()))

# result = bisect_right(arr, x) - bisect_left(arr, x)

# if result == 0:
#     print(-1)
# else:
#     print(result)

def search(arr, target, start, end):
    mid = 0
    while start <= end:
        mid = (start + end) // 2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return None

def solve(target):
    left = 0
    right = 0
    while target != 0:
        if arr[target] == arr[target - 1]:
            target -= 1
        else:
            left = target
            break
    while target != n - 1:
        if arr[target] == arr[target + 1]:
            target += 1
        else:
            right = target + 1
            break
    print(right - left)

target = search(arr, x, 0, n - 1)
if target == None:
    print(-1)
else:
    solve(target)
      
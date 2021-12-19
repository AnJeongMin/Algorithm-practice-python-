n, m = map(int, input().split())

arr = list(map(int, input().split()))

def solve(arr, start, end):
    result = 0
    while start <= end:
        total = 0
        mid = (start + end) // 2
        for x in arr:
            if x > mid:
                total += x - mid
        if total < m:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result
        
print(solve(arr, 0, max(arr)))

# 범위 커지면 매우 느려짐 O(n)
# result = 0
# height = max(arr)

# while result < m:
#     print(height)
#     result = 0
#     for i in range(n):
#         if arr[i] - height >= 0:
#             result += arr[i] - height
#     if height == 0:
#         print("None")
#         break
#     height -= 1

# print(height + 1)

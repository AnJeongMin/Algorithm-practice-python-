import time

start = time.time()

arr = list(map(int, input().split()))
sum = int(input())

# def solve():
#     start, end = 0, 0
#     temp = 0
#     cnt = 0
#     while True:
#         if start > len(arr) - 1 or end > len(arr) - 1:
#             break
#         for x in arr[start:end + 1]: temp += x
#         if temp >= sum:
#             start += 1
#             if temp == sum:
#                 cnt += 1
#         else:
#             end += 1
#         temp = 0
#     return cnt

def solve():
    end = 0
    cnt = 0
    temp = 0
    for start in range(len(arr)):
        while temp < sum and end < len(arr):
            temp += arr[end]
            end += 1
        if temp == sum:
            cnt += 1
        temp -= arr[start]
    return cnt

print(solve())

end = time.time()

print(end - start)
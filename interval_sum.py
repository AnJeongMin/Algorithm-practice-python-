arr = list(map(int, input().split()))
n = int(input())
query = [() for _ in range(n)]
for i in range(n):
    left, right = map(int, input().split())
    query[i] = (left, right)

# O(n + m)
# def solve():
#     sum = [0] * n

#     for i in range(n):
#         x = query[i]
#         for j in range(x[0], x[1] + 1):
#             sum[i] += arr[j]

#     for i in range(n):
#         print(query[i], ":", sum[i])

prefix_sum = [0] * len(arr)
temp = 0
for i in range(len(arr)):
    temp += arr[i]
    prefix_sum[i] = temp

def solve():
    for i in query:
        sum = prefix_sum[i[1]] - prefix_sum[i[0] - 1]
        print(i, sum) 

solve()
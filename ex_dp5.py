n = int(input())
arr = list(map(int, input().split()))

def solve(arr, n):
    dp = [1] * n
    arr.reverse()
    # LIS algorithm
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return n - max(dp)
    
print(solve(arr, n))
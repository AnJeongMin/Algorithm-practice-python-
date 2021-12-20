n = int(input())

def solve():
    r, c = map(int, input().split())
    arr = list(map(int, input().split()))
    dp = [] 
    cnt = 0
    for _ in range(r):
        dp.append(arr[cnt:cnt + c]) 
        cnt += c
    for i in range(1, c):
        for j in range(r):
            if j == 0:
                left_up = 0
            else:
                left_up = dp[j - 1][i - 1]
            if j == r - 1:
                left_down = 0
            else:
                left_down = dp[j + 1][i - 1]
            left = dp[j][i - 1]
            dp[j][i] += max(left, left_up, left_down)
    result = []
    for i in range(r): 
        result.append(dp[i][c - 1])
    return max(result)
    
for _ in range(n):
    print(solve())
    
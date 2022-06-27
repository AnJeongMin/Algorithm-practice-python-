import sys
sys.stdin = open("input.txt", "r")

def solve(pos, limit, arr):
    res = 0
    dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    dp = [[[0] * c for _ in range(r)] for _ in range(limit+1)] # dp[k][y][x]
    
    for i in range(r): # k=1 initialize
        for j in range(c): 
            cnt = 0
            if arr[i][j] == "X":
                continue
            for dx, dy in dir:
                if 0 <= j+dx < c and 0 <= i+dy < r:
                    continue
                cnt += 1
            dp[1][i][j] = cnt
 
    for i in range(2, limit+1): # 500
        temp = [[0]*c for _ in range(r)]
        for j in range(r): # 100
            for k in range(c): # 100
                for dx, dy in dir: # 4
                    tx, ty = k+dx, j+dy  
                    if is_range(k+dx, j+dy):
                        temp[j][k] += dp[i-1][ty][tx]
  
        for j in range(r): # 100
            for k in range(c): # 100
                dp[i][j][k] += temp[j][k]

    for limit in range(1, limit+1):
        res += dp[limit][pos[1]][pos[0]]

    return res%1000000007

def is_range(x, y):
    return 0 <= x < c and 0 <= y < r and arr[y][x] != "X"

K = int(input())
for k in range(K):
    r, c, num = map(int, input().split())
    pos = 0
    arr = []
    for i in range(r):
        temp = list(input())
        for j in range(c):
            if temp[j] == "S":
                temp[j] = "."
                pos = (j, i)
        arr.append(temp)
    print("#{} {}".format(k+1, solve(pos, num, arr)))
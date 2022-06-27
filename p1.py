import sys
from collections import deque
sys.stdin = open("input.txt", "r")

def solve(arr, oils): # arr 300, 300 || max K 400 || D 20,000
    res = 0

    q = []
    for row in arr:
        for elem in row:
            q.append(elem)
    q.sort()
    
    dq = deque()
    for elem in q:
        dq.append([elem, 0])

    day = 1
    for oil in oils: # 20,000
        for _ in range(oil): # 400
            cut, cutday = dq.pop()
            dq.appendleft([1, day])
            grow = day-cutday
            res += (cut-1+grow)*day
        day += 1
 
    return res

K = int(input())

for k in range(K):
    r, c, d = map(int, input().split()) # y, x, day
    arr = [list(map(int, input().split())) for _ in range(r)]
    oils = list(map(int, input().split()))

    print("#{} {}".format(k+1, solve(arr, oils)))
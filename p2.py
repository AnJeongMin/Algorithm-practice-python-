import sys
from collections import deque
sys.stdin = open("input.txt", "r")

def solve(r, c, x, y, arr):
    visited = {}
    q = deque([(x, y, 0, 0, 0, 0)]) # x, y, A, B, C, cnt
    visited[(x, y, 0, 0, 0)] = True
    while q:
        x, y, A, B, C, cnt = q.popleft()
        print(x, y, A, B, C, cnt)
        if arr[y][x] == "S" and (A, B, C) == (1, 1, 1):
            return cnt
        for dx, dy in dir:
            tx, ty = x+dx, y+dy
            ta, tb, tc = A, B, C
            if is_range((tx, ty, A, B, C), visited):
                next = arr[ty][tx]
                if next == "A":
                    ta = 1
                elif next == "B":
                    tb = 1
                elif next == "C":
                    tc = 1
                elif next == "X": 
                    if (A, B, C) != (1, 1, 1):
                        continue
                visited[(tx, ty, ta, tb, tc)] = True
                q.append((tx, ty, ta, tb, tc, cnt+1))

def is_range(info, visited):
    x, y, A, B, C = info
    return 0 <= x < c and 0 <= y < r and (x, y, A, B, C) not in visited

K = int(input())
dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]

for k in range(K):
    r, c, y, x = map(int, input().split())
    arr = [list(input()) for _ in range(r)]
    print("#{} {}".format(k+1, solve(r, c, x-1, y-1, arr)))
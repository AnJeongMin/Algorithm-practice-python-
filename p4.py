import sys
from collections import deque
sys.stdin = open("input.txt", "r")

def solve(src, dst, graph, dic):

    q = deque()
    visited = {}
    for x in dic[src]:
        q.append((src, x, 1)) 
        visited[(src, x)] = 1 # visited 판별 시 0이면 false를 반환하므로 +1 후 결과에 -1
    
    res = 1e9
    while q:
        now, line, cnt = q.popleft()
        if now == dst:
            res = min(res, cnt-1)
        for next in graph[now]:
            for nline in dic[next]:
                if visited.get((next, nline)) and visited[(next, nline)] <= cnt:
                    continue
                if line == nline:
                    q.appendleft((next, nline, cnt))
                    visited[(next, nline)] = cnt
                elif nline in dic[now]:
                    q.append((next, nline, cnt+1))
                    visited[(next, nline)] = cnt+1
        
    if res == 1e9:
        res = -1
    return res

K = int(input())
for k in range(K):
    n, m, src, dst = map(int, input().split())
    leng = list(map(int, input().split()))

    graph = [[] for _ in range(n+1)]
    dic = {i: [] for i in range(1, n+1)}
    for i in range(1, m+1):
        temp = list(map(int, input().split()))
        for j in range(1, leng[i-1]):
            graph[temp[j]].append(temp[j-1]) # 연결된 역들을 연결
            graph[temp[j-1]].append(temp[j]) # 역방향
        for x in temp:
            dic[x].append(i) # 각 역마다 갈 수있는 노선

    print("#{} {}".format(k+1, solve(src, dst, graph, dic)))

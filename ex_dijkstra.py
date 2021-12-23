import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())

graph = [[] for i in range(n + 1)]

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
    
distance = [INF] * (n + 1)

def solve(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        for i in graph[now]:
            if distance[i[0]] < dist:
                continue
            else:
                distance[i[0]] = dist + i[1]
                heapq.heappush(q, (distance[i[0]], i[0]))
    cnt = 0
    max = 0
    for i in range(n + 1):
        if distance[i] != INF:
            cnt += 1 
            if max < distance[i]:
                max = distance[i]
    return cnt - 1, max

result = solve(c)
print(result[0], result[1])
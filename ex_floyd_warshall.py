import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

dist = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    dist[a][b] = 1
    dist[b][a] = 1
    
x, k = map(int, input().split())

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            dist[a][b] = 0

for k in range(n + 1):
    for a in range(n + 1):
        for b in range(n + 1):
            dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])
        
result = dist[1][k] + dist[k][x]

if result >= INF:
    print(-1)
else:
    print(result)

import sys
input = sys.stdin.readline
INF = int(1e9)

def bf(start):
    dist[start] = 0
    for i in range(n):
        for j in range(m):
            now = edges[j][0]
            next = edges[j][1]
            cost = edges[j][2]
            if dist[now] != INF and dist[next] > dist[now] + cost:
                dist[next] = dist[now] + cost
                if i == n - 1:
                    return True
    return False

n, m = map(int, input().split())
edges = []
dist = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

if bf(1) == True:
    print("Negative Cycle")
else:
    for i in range(1, n + 1):
        if dist[i] == INF:
            print("INFINTY")
        else:
            print(i, "th :",dist[i])

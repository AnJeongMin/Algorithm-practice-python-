import sys
from collections import deque
INF = int(1e9)

def solve(n, graph, c, src, dst):

    result = 0

    f = [[0]*(n+1) for _ in range(n+1)]
    
    # O(VE^2)
    while True: # O(VE)
        v = [-1] * (n+1)
        q = deque()
        q.append(src)
        while q: # O(E)
            now = q.popleft()
            for next in graph[now]:
                if c[now][next] > f[now][next] and v[next] == -1:
                    q.append(next)
                    v[next] = now # path trace
                    if next == dst: break 
            
        if v[dst] == -1: break # 모든 길 탐색 완료 
        
        flow = INF
        tmp = dst
        while tmp != src:
            # 흐를 수 있는 유량의 최소값
            flow = min(flow, c[v[tmp]][tmp] - f[v[tmp]][tmp])
            tmp = v[tmp]
        
        tmp = dst
        while tmp != src:
            f[v[tmp]][tmp] += flow
            f[tmp][v[tmp]] -= flow
            tmp = v[tmp]

        result += flow

    print(result)
    return
        

if __name__ == "__main__":

    n, e = map(int, input().split())
    graph = [[]*(n+1) for _ in range(n+1)]
    c = [[0]*(n+1) for _ in range(n+1)]

    for _ in range(e):
        a, b, cost = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        c[a][b] = cost

    src, dst = map(int, input().split())

    solve(n, graph, c, src, dst)

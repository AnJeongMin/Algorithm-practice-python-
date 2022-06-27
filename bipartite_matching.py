def solve(n, m, graph):

    occupy = [0] * (m+1)
    cnt = 0
    for i in range(1, n+1):
        visited = [False] * (n+1)
        if dfs(i, graph, occupy, visited):
            cnt += 1

    print(cnt)
    for i in range(1, n+1):
        print("{} -> {}".format(occupy[i], i))
    return

# occupy: 현재 점유중인 노드, visited: 이미 할당 됨
def dfs(x, graph, occupy, visited):
    for tar in graph[x]:
        if visited[tar]: continue
        visited[tar] = True
        if not occupy[tar] or dfs(occupy[tar], graph, occupy, visited):
            occupy[tar] = x
            return True
    return False

if __name__ == "__main__":

    n, m, e = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)

    solve(n, m, graph)

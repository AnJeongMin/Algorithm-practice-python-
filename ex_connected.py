def dfs(x, y):
    if x <= -1 or x >= row or y <= -1 or y >= col:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False
        
row, col = map(int, input().split())

graph = []
for i in range(row):
    graph.append(list(map(int, input())))
    
result = 0

for i in range(row):
    for j in range(col):
        if dfs(i, j):
            result += 1
            
print(result)

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a, b = find_parent(parent, a), find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())

parent = [0] * (v + 1)

for i in range(v + 1):
    parent[i] = i

edges = []
for i in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

total_cost = 0

for i in range(e):
    cost, a, b = edges[i]
    if find_parent(parent, a) == find_parent(parent, b):
        continue
    else:
        union_parent(parent, a, b)
        total_cost += cost

# for i in range(1, v + 1):
#     find_parent(parent, i)

# for i in range(1, v + 1):
#     print("Root of", i, "is", parent[i], end = ', ')
# print()
print("Total cost is :", total_cost)
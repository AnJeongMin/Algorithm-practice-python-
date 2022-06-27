import heapq
import sys
sys.setrecursionlimit(int(1e5))
INF = int(1e3)

SPOT_NUM = 39

def path_trace(src, dst, path, temp):

    if path[dst] == src:
        temp.append(src)
        return temp
    else:
        temp.append(path[dst])
        path_trace(src, path[dst], path, temp)
    return temp

def dijstra(src, dst):

    q = []
    heapq.heappush(q, (0, src))
    distance[src] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dist < distance[now]:
            continue
        for i in graph[now]:
            next, cost = i, 1+dist
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q, (cost, next))
                path[next] = now
        
    temp = [dst]
    result = path_trace(src, dst, path, temp)
    result.reverse()
    
    print("\npath: ", end=' ')
    for x in result:
        print(x, end=' ')
    print()
    return

if __name__ == "__main__":

    graph = [[1, 13], [0, 2, 14], [1, 3, 4, 15], [2, 16], [2, 5, 17], [4, 6, 18], [5, 7, 19], [6, 8, 10, 20],\
            [7, 9, 21], [8, 22], [7, 11, 23], [10, 12, 24], [11, 25], [0, 14, 26], [1, 13, 15, 27], [2, 14, 16, 17, 28],\
            [3, 15, 29], [4, 15, 18, 30], [5, 17, 19, 31], [6, 18, 20, 32], [7, 19, 21, 23, 33], [8, 20, 22, 34],\
            [9, 21, 35], [10, 20, 24, 36], [11, 23, 25, 37], [12, 24, 38], [13, 27], [14, 26, 28], [15, 27, 29, 30],\
            [16, 28], [17, 28, 31], [18, 30, 32], [19, 31, 33], [20, 32, 34, 36], [21, 33, 35], [22, 34], [23, 33,37],\
            [24, 36, 38], [25, 37]]
    
    src, dst = map(int, input("src, dst: ").split())

    distance = [INF] * SPOT_NUM
    path = [0] * SPOT_NUM

    dijstra(src, dst)



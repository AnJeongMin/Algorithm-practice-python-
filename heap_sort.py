import sys
import heapq
input = sys.stdin.readline

def heap_sort(iterable):
    h = []
    result = []
    
    for value in iterable:
        heapq.heappush(h, value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

n = int(input())
arr = []

arr = list(map(int, input().split()))

res = heap_sort(arr)

for i in range(n):
    print(res[i], end = ' ')
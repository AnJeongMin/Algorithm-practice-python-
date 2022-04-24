from random import randint
from collections import deque
import time

start = time.time()

arr = [13, 7, 5, 17, 9, 12, 0, 16, 10, 3, 1, 11, 6, 2, 4, 8, 15, 19, 14, 18]
arr_rand = []
for _ in range(100):
    arr_rand.append(randint(1, 100))
result = []

# selection sort : O(n2)
def selection_sort(iterable):
    arr = iterable
    for i in range(len(arr)):
        min_index = i
        for j in range(1 + i, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# insertion sort : worst O(n2), best O(n)
def insertion_sort(iterable):
    arr = iterable
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else: 
                break  
    return arr

# quick sort : normal O(nlogn), worst O(n2)
def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right:
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)
    return arr
    
# quick sort(python ver)
def quick_sort_py(arr):
    if len(arr) <= 1:
        return arr 
    pivot = arr[0]
    tail = arr[1:]
    
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    
    return quick_sort_py(left_side) + [pivot] + quick_sort_py(right_side)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    i, j = 0, 0
    result = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1

    return result

def heapify(arr, i, n):
    l = i*2+1
    r = l+1
    idx = i

    if l < n and arr[l] > arr[i]: idx = l
    if r < n and arr[r] > arr[idx]: idx = r
    if idx != i:
        arr[i], arr[idx] = arr[idx], arr[i]
        heapify(arr, idx, n)

def heap_sort(arr):
    n = len(arr)
    for i in range(n-1, -1, -1):
        heapify(arr, i, n-1)
    for i in range(n-1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)
    return arr

# counting sort : O(n + k) -> k = max(array)
def counting_sort(arr):
    count = [0] * (max(arr) + 1)
    for i in range(len(arr)):
        count[arr[i]] += 1
        
    for i in range(len(count)):
        for j in range(count[i]):
            result.append(i)
            
    return result

# radix sort : O(d * (n + k)) -> d = 최대 자리수, k = 10
def radix_sort(arr):
    qs = [deque() for _ in range(len(arr))]

    max_v = max(arr)
    q = deque(arr)
    digit = 1

    while max_v >= digit:
        while q:
            num = q.popleft()
            qs[(num//digit)%10].append(num)
        
        for queue in qs:
            while queue:
                q.append(queue.popleft())

        digit *= 10

    return list(q)

# print

result = merge_sort(arr_rand)

end = time.time()

print(result)
print(end - start)

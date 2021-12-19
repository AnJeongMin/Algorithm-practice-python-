from random import randint
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

# counting sort : O(n + k) -> k = max(array)
def counting_sort(arr):
    count = [0] * (max(arr) + 1)
    result = []
    for i in range(len(arr)):
        count[arr[i]] += 1
        
    for i in range(len(count)):
        for j in range(count[i]):
            result.append(i)
            
    return result

# print

result = quick_sort_py(arr_rand)

end = time.time()

print(result)
print(end - start)

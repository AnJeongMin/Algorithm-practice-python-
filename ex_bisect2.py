from bisect import bisect_left, bisect_right

def count_elements(arr , left_value, right_value):
    return bisect_right(arr, right_value) - bisect_left(arr, left_value)

arr = [1, 2, 3, 3, 3, 4, 4, 8, 9]
print(bisect_left(arr, 3), bisect_right(arr, 3))
print(count_elements(arr, 3, 3)) # 값이 3인 데이터 개수

print(count_elements(arr, 3, 4)) # 3 <= X <= 4, X 개수
import time

start = time.time()

d = [0] * 100

# O(2^n)
def fibonacci_recur(n):
    if 1 <= n <= 2:
        return 1
    return fibonacci_recur(n - 1) + fibonacci_recur(n - 2)

# O(n)
def fibonacci_dp(n):
    arr = [1, 1]
    while len(arr) < n:
        index = len(arr) - 1
        arr.append(arr[index] + arr[index - 1])
    return arr[len(arr) - 1]

def fibo_TtoB(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo_TtoB(x - 1) + fibo_TtoB(x - 2)
    return d[x]
    
def fibo_BtoT(x):
    d[1], d[2] = 1, 1
    n = 99
    for i in range(3, n + 1):
        d[i] = d[i - 1] + d[i - 2]
    return d[x]    
    
result = fibo_TtoB(99)

end = time.time()

print(result, format(end - start, ".9f"))


target = int(input())
arr_prime = [1] * (target + 1)

for i in range(2, int(target**(1/2) + 1)):
    if arr_prime[i] == 1:
        j = 2
        while i * j <= target:
            arr_prime[i * j] = 0
            j += 1

for i in range(2, target):
    if arr_prime[i] == 1:
        print(i, end = ' ')


        


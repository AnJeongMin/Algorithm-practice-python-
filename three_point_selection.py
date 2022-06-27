from collections import defaultdict

def solve(n, arr):
    res = 0

    gradient_dic = defaultdict(set)
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[i][0] == arr[j][0]:
                gradient_dic[(arr[i][0], -1, -1)].update([i, j])
            elif arr[i][1] == arr[j][1]:
                gradient_dic[(-1, arr[i][1], -1)].update([i, j])
            else:
                gradient = (arr[i][1]-arr[j][1])/(arr[i][0]-arr[j][0])
                xpos = -arr[i][1]/gradient + arr[i][0]
                ypos = -arr[i][0]*gradient + arr[i][1]
                gradient_dic[(xpos, ypos, gradient)].update([i, j])

    for _, value in list(gradient_dic.items()):
        if len(value) > 2:
            res += combi_calc(len(value))
    return res

def combi_calc(x):
    res = 1
    for i in range(x, x-3, -1):
        res *= i
    return res//6
    
n = 7
arr = [[0, 0], [1, 1], [2, 2], [3, 2], [3, 3], [4, 2], [5, 1]]
print(solve(n, arr))
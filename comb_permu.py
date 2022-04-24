def permutation(idx, depth):
    if depth == len(arr):
        temp = [x for x in list]
        perm.append(temp)
        return
    
    for i, val in enumerate(arr):
        if not visited[i]:
            visited[i] = True
            list.append(val)
            permutation(idx+1, depth+1)
            list.pop()
            visited[i] = False

def combination(idx, depth):
    if depth == len(arr):
        temp = [i for i in range(len(arr)) if visited[i]] 
        comb.append(temp)
        return
    
    for i in range(idx, len(arr)):
        if not visited[i]:
            visited[i] = True
            combination(i+1, depth+1)
            visited[i] = False

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]

    visited = [False] * 6

    list = []
    perm = []
    comb = []

    permutation(0, 3)
    combination(0, 3)
    for i in perm:
        print(i)
    print(len(perm))
    print(" ")
    for i in comb:
        print(i)
    print(len(comb))

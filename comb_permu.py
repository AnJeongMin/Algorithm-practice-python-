result = []

def solution(orders, course):
    global result
    
    answer = []
    
    for t in course:
        dic = {}
        for arr in orders:
            visited = [False] * (len(orders[0]))
            com(0, 0, sorted(list(arr)), visited, t)
            for x in result:
                if dic.get(x): dic[x] += 1
                else: dic[x] = 1
            result.clear()
        temp = list(dic.items())
        maxv = 2 # 2개 이상
        candi = []
        for x in temp:
            if x[1] > maxv:
                candi.clear()
                candi.append(x[0])
                maxv = x[1]
            elif x[1] == maxv:
                candi.append(x[0])
        for y in candi: answer.append(y)
        
        answer.sort()
    return answer

def com(idx, depth, arr, visited, tar):
    global result
    
    if depth == tar:
        comb = [arr[i] for i in range(len(arr)) if visited[i] == True]
        result.append("".join(comb))
        return
    
    for i in range(idx, len(arr)):
        if visited[i] == False:
            visited[i] = True
            com(i+1, depth+1, arr, visited, tar)
            visited[i] = False

orders = ["XYZ", "ABCXY"]
course = [2, 3, 4]
print(solution(orders, course))
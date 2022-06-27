import sys
sys.stdin = open("input.txt", "r")

dic = ["ENFJ", "ENFP", "ENTJ", "ENTP", "ESFJ", "ESFP", "ESTJ", "ESTP",\
        "INFJ", "INFP", "INTJ", "INTP", "ISFJ", "ISFP", "ISTJ", "ISTP"]

def solve(n, arr):
    str_dic = {"E": 0, "N": 0, "F": 0, "J": 0, "I": 0, "S": 0, "T": 0, "P": 0}
    dfs(0, 0, str_dic)
    return res

def dfs(idx, money, now_dic):
    global res

    if money > res:
        return
    if now_dic["E"] >= n and now_dic["N"] >= n and now_dic["F"] >= n and now_dic["J"] >= n\
        and now_dic["I"] >= n and now_dic["S"] >= n and now_dic["T"] >= n and now_dic["P"] >= n:
        res = min(res, money)

    for i in range(idx, 16):
        for str in dic[i]:
            now_dic[str] += 1
        dfs(i+1, money+arr[i], now_dic)
        for str in dic[i]:
            now_dic[str] -= 1
    return 
     
K = int(input())
for k in range(K):
    n = int(input())
    arr = list(map(int, input().split()))
    res = 1e9
    print("#{} {}".format(k+1, solve(n, arr)))

from collections import deque

def solution(q1, q2):
    sum1, sum2 = sum(q1), sum(q2) # popleft, append only

    cnt = 0
    while sum1 != sum2:
        if sum1 > sum2:
            temp = q1.popleft()
            sum1 -= temp
            q2.append(temp)
            sum2 += temp
        elif sum1 < sum2:
            temp = q2.popleft()
            sum2 -= temp
            q1.append(temp)
            sum1 += temp
        cnt += 1
        if cnt > 1000000:
            return -1

    return cnt

if __name__ == "__main__":

    q1, q2 = deque(), deque()
    q1.extend([1, 1])
    q2.extend([1, 5])

    print(solution(q1, q2))

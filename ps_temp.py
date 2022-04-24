def solve():

    result = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                now = arr[i][j]
                q = [(j, i)]
                visited[i][j] = True
                while q:
                    x, y = q.pop()
                    for d in dir:
                        dx, dy = x+d[0], y+d[1]
                        if 0 <= dx < n and 0 <= dy < n:
                            if not visited[dy][dx] and arr[dy][dx] == now:
                                visited[dy][dx] = True
                                q.append((dx, dy))
                result += 1
    return result

if __name__ == "__main__":

    n = int(input())
    arr = [list(input()) for _ in range(n)]

    dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    a = solve()

    for i in range(n):
        for j in range(n):
            if arr[i][j] == "R" or arr[i][j] == "G":
                arr[i][j] = "Y"

    b = solve()

    print(a, b)  
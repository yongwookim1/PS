n = int(input())

graph = [list(input()) for _ in range(n)]

ng = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] != ".":
            ng[i][j] = "*"
        else:
            number = 0
            for dx, dy in [
                (-1, -1),
                (0, 1),
                (1, 1),
                (1, 0),
                (1, -1),
                (0, -1),
                (-1, 1),
                (-1, 0),
            ]:
                nx, ny = i + dx, j + dy
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] != ".":
                        number += int(graph[nx][ny])
            if number < 10:
                ng[i][j] = number
            elif number >= 10:
                ng[i][j] = "M"


for i in ng:
    print(*i, sep="")

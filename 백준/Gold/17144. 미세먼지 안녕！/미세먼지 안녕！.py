from collections import deque
import copy

n, m, t = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

ap = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == -1:
            ap.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(queue, ng):
    while queue:
        x, y = queue.popleft()
        st = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[x][y] > 0 and graph[nx][ny] != -1:
                    ng[nx][ny] += int(graph[x][y] / 5)
                    st += 1
        ng[x][y] -= int(graph[x][y] / 5) * st
        ng[x][y] += graph[x][y]
    return ng


def wind(x, y):
    ap1, ap2 = ap[0], ap[1]
    if (x, y) != ap1 and (x, y) != ap2:
        if y == 0 and x < ap1[0]:
            ng[x + 1][y] = graph[x][y]
        elif x != 0 and y == m - 1 and x <= ap1[0]:
            ng[x - 1][y] = graph[x][y]
        elif x == 0 and y != 0:
            ng[x][y - 1] = graph[x][y]
        elif x == ap1[0] and y != 0 and y != m - 1:
            ng[x][y + 1] = graph[x][y]

        elif y == 0 and x > ap2[0]:
            ng[x - 1][y] = graph[x][y]
        elif x != n - 1 and y == m - 1 and x >= ap2[0]:
            ng[x + 1][y] = graph[x][y]
        elif x == n - 1 and y != 0:
            ng[x][y - 1] = graph[x][y]
        elif x == ap2[0] and y != 0 and y != m - 1:
            ng[x][y + 1] = graph[x][y]

    ng[ap1[0]][ap1[1]] = -1
    ng[ap2[0]][ap2[1]] = -1
    ng[ap1[0]][ap1[1] + 1] = 0
    ng[ap2[0]][ap2[1] + 1] = 0
    return ng


for _ in range(t):
    queue = deque()
    ng = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                queue.append((i, j))
            elif graph[i][j] == -1:
                ng[i][j] = -1
    graph = bfs(queue, ng)
    ng = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            ng = wind(i, j)
    graph = copy.deepcopy(ng)

r = 2
for i in range(n):
    for j in range(m):
        r += ng[i][j]

print(r)

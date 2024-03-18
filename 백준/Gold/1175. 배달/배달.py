from collections import deque

n, m = map(int, input().split())

graph = []
c = 0
for i in range(n):
    graph.append(list(input()))
    for j in range(m):
        if graph[i][j] == "S":
            start = (i, j)
        elif graph[i][j] == "C":
            graph[i][j] = c
            c += 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    queue = deque([(*start, 0, 0, 4)])
    visited = [[[[0] * m for _ in range(n)] for _ in range(5)] for _ in range(3)]
    while queue:
        y, x, t, bit, d = queue.popleft()
        if visited[bit][d][y][x]:
            continue
        visited[bit][d][y][x] = 1
        if type(graph[y][x]) == int:
            bit |= 1 << graph[y][x]
        if bit == 3:
            return t
        for i in range(4):
            if i == d:
                continue
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] != "#":
                queue.append((ny, nx, t + 1, bit, i))
    return -1


print(bfs())

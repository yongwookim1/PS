from collections import deque
from itertools import combinations

n, m = map(int, input().split())

graph = []
home = []
chicken = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] == 1:
            home.append((i, j))
        elif graph[i][j] == 2:
            chicken.append((i, j))


def bfs(queue, visited):
    dist = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if graph[nx][ny] == 0 or graph[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
                elif graph[nx][ny] == 2:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
                    dist.append((nx, ny, visited[nx][ny]))
    return sorted(dist)


result = []
for i in range(len(home)):
    queue = deque()
    queue.append(home[i])
    visited = [[0] * n for _ in range(n)]
    result.append(bfs(queue, visited))

e = []
for i in combinations(range(len(chicken)), m):
    ct = 0
    for j in range(len(home)):
        r = float("inf")
        for k in i:
            if result[j][k][2] < r:
                r = result[j][k][2]
        ct += r
    e.append(ct)

print(min(e))

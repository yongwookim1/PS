from collections import deque
from itertools import combinations

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))


def bfs(queue, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 0 or graph[nx][ny] == 2:
                    if visited[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx, ny))
    r = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 1 and visited[i][j] == 0:
                return False
            elif visited[i][j] > r:
                r = visited[i][j]
    return r


start_points = [(i, j) for j in range(n) for i in range(n) if graph[i][j] == 2]

result = []
for start_point in combinations(start_points, m):
    queue = deque()
    visited = [[0] * n for _ in range(n)]
    for i in start_point:
        queue.append(i)
        p, q = i
        visited[p][q] = 1
    b = bfs(queue, visited)
    if b:
        result.append(b - 1)

print(min(result) if result else -1)

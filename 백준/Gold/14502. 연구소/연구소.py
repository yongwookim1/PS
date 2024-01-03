from collections import deque
from itertools import permutations
from copy import deepcopy

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

graph2 = deepcopy(graph)
zerozone = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            zerozone.append((i, j))

queue = deque()
queue2 = deepcopy(queue)

visited = [[0] * m for _ in range(n)]
visited2 = deepcopy(visited)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph, queue, visited):
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                if graph[nx][ny] == 2:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    continue
                elif graph[nx][ny] == 1:
                    continue
                elif graph[nx][ny] == 0:
                    graph[nx][ny] = 2
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
    st = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                st += 1
    return st


mx = 0
for i in permutations(zerozone, 3):
    graph = deepcopy(graph2)
    visited = deepcopy(visited2)
    queue = deepcopy(queue2)
    for j, k in i:
        graph[j][k] = 1
    for p in range(n):
        for q in range(m):
            if graph[p][q] == 2:
                queue.append((p, q))
    mx = max(bfs(graph, queue, visited), mx)

print(mx)

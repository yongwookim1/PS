from collections import deque
from copy import deepcopy


n = int(input())

graph = [list(input()) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def divide(queue, visited):
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
                if graph[nx][ny] == ".":
                    visited[nx][ny] = True
                    graph[nx][ny] = nb
                    queue.append((nx, ny))


nb = 1
nbl = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == ".":
            queue = deque()
            queue.append((i, j))
            visited = [[False] * n for _ in range(n)]
            visited[i][j] = True
            graph[i][j] = nb
            divide(queue, visited)
            nbl.append(nb)
            nb += 1

graph2 = deepcopy(graph)


def bfs(queue: deque, visited: list, nb: int):
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
                if graph[nx][ny] == nb:
                    visited[nx][ny] = True
                    queue.append((nx, ny))


ct = 0
for i in range(n):
    for j in range(n):
        st = 0
        graph = deepcopy(graph2)
        visited = [[False] * n for _ in range(n)]
        for nb in nbl:
            if graph[i][j] == nb:
                graph[i][j] = "S"
                for p in range(n):
                    for q in range(n):
                        if graph[p][q] == nb and visited[p][q] == False:
                            queue = deque()
                            queue.append((p, q))
                            visited[p][q] = True
                            bfs(queue, visited, nb)
                            st += 1
                if st >= 2:
                    ct += 1

print(ct)

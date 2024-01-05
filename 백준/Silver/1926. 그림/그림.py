from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

visited = [[0] * m for _ in range(n)]

queue = deque()


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs():
    st = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    continue
                elif graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    st += 1
                    queue.append((nx, ny))
    return st


st = 0
mx = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            queue.append((i, j))
            mx = max(bfs(), mx)
            st += 1

print(st, mx)

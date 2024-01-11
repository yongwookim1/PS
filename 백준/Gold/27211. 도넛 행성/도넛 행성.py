from collections import deque

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(queue):
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nx, ny = nx % n, ny % m
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))


st = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and visited[i][j] == False:
            queue = deque()
            queue.append((i, j))
            bfs(queue)
            st += 1

print(st)

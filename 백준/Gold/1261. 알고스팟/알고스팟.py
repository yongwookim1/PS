from collections import deque

m, n = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

visited = [[-1] * m for i in range(n)]
visited[0][0] = 0

queue = deque()
queue.append((0, 0))


def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                if graph[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
                elif graph[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y]
                    queue.appendleft((nx, ny))
    return visited[n - 1][m - 1]


print(bfs())

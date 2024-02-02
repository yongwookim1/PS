from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(input()))
    for j in range(m):
        if graph[i][j] == "S":
            start = (i, j, 0)
        elif graph[i][j] == "H":
            home = (i, j, 1)
queue = deque()
queue.append(start)

visited = [[[-1] * 2 for _ in range(m)] for _ in range(n)]
visited[start[0]][start[1]][0] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(queue, visited):
    while queue:
        x, y, k = queue.popleft()
        if (x, y, k) == home:
            return visited[x][y][k]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny][k] == -1:
                if graph[nx][ny] == "E" or graph[nx][ny] == "S":
                    visited[nx][ny][k] = visited[x][y][k] + 1
                    queue.append((nx, ny, k))
                elif graph[nx][ny] == "F":
                    visited[nx][ny][1] = visited[x][y][k] + 1
                    queue.append((nx, ny, 1))
                elif graph[nx][ny] == "H":
                    visited[nx][ny][k] = visited[x][y][k] + 1
                    queue.append((nx, ny, k))
    return -1


print(bfs(queue, visited))

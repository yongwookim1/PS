from collections import deque

n, m, k = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(input()))
    for j in range(m):
        if graph[i][j] == "S":
            start = (i, j, 0)
            graph[i][j] = "."

queue = deque()
queue.append(start)

visited = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]
visited[start[0]][start[1]][start[2]] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(queue, visited):
    while queue:
        x, y, f = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny][f] == 0:
                if graph[nx][ny] == ".":
                    visited[nx][ny][f] = visited[x][y][f] + 1
                    queue.append((nx, ny, f))
                elif graph[nx][ny] == str(f + 1):
                    visited[nx][ny][f + 1] = visited[x][y][f] + 1
                    queue.append((nx, ny, f + 1))
                elif graph[nx][ny] == "X":
                    continue
                else:
                    visited[nx][ny][f] = visited[x][y][f] + 1
                    queue.append((nx, ny, f))
                if graph[nx][ny] == str(k) and f == k - 1:
                    return visited[nx][ny][f + 1] - 1


print(bfs(queue, visited))

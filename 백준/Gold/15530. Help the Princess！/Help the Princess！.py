from collections import deque

n, m = map(int, input().split())

graph = []
soldiers = []
for i in range(n):
    graph.append(list(input()))
    for j in range(m):
        if graph[i][j] == "%":
            door = (i, j, 0)
            graph[i][j] = "."

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(queue, visited):
    pr = 4001
    sr = 4001
    while queue:
        x, y, d = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False:
                if graph[nx][ny] == ".":
                    visited[nx][ny] = True
                    queue.append((nx, ny, d + 1))
                elif graph[nx][ny] == "@":
                    visited[nx][ny] = True
                    queue.append((nx, ny, d + 1))
                    pr = d + 1
                elif graph[nx][ny] == "$":
                    visited[nx][ny] = True
                    queue.append((nx, ny, d + 1))
                    if d + 1 < sr:
                        sr = d + 1
    return pr, sr


queue = deque()
queue.append(door)

visited = [[False] * m for _ in range(n)]
visited[door[0]][door[1]] = True

pr, sr = bfs(queue, visited)

print("Yes") if pr < sr else print("No")

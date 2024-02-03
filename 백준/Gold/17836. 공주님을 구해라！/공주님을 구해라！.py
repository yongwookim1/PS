from collections import deque

n, m, t = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[[-1] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 0

queue = deque()
queue.append((0, 0, 0))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(queue, visited):
    while queue:
        x, y, s = queue.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][s]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny][s] == -1:
                if graph[nx][ny] == 0:
                    visited[nx][ny][s] = visited[x][y][s] + 1
                    queue.append((nx, ny, s))
                elif graph[nx][ny] == 2:
                    visited[nx][ny][s + 1] = visited[x][y][s] + 1
                    queue.append((nx, ny, s + 1))
                elif graph[nx][ny] == 1 and s == 1:
                    visited[nx][ny][s] = visited[x][y][s] + 1
                    queue.append((nx, ny, s))
    return False


r = bfs(queue, visited)

if r and r <= t:
    print(r)
else:
    print("Fail")

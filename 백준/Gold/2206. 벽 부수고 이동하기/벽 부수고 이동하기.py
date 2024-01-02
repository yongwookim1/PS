from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

visited = [[[0] * 2 for i in range(m)] for j in range(n)]
visited[0][0][1] = 1

queue = deque()
queue.append((0, 0, 1))


def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x, y, w = queue.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][w]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and w == 1 and visited[nx][ny][w] == 0:
                    visited[nx][ny][w - 1] = visited[x][y][w] + 1
                    queue.append((nx, ny, 0))
                elif graph[nx][ny] == 0 and visited[nx][ny][w] == 0:
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    queue.append((nx, ny, w))
    return -1


print(bfs())

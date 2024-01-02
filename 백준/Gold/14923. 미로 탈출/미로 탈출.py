from collections import deque

n, m = map(int, input().split())
hx, hy = map(int, input().split())
ex, ey = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

visited = [[[0] * 2 for i in range(m)] for j in range(n)]


def bfs(graph):
    queue = deque()
    queue.append((hx - 1, hy - 1, 1))
    visited[hx - 1][hy - 1][1] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x, y, w = queue.popleft()
        if x == ex - 1 and y == ey - 1:
            return visited[x][y][w]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue
            elif graph[nx][ny] == 1 and w == 1 and visited[nx][ny][w] == 0:
                queue.append((nx, ny, w - 1))
                visited[nx][ny][w - 1] = visited[x][y][w] + 1
            elif graph[nx][ny] == 1 and w == 0:
                continue
            elif graph[nx][ny] == 0 and visited[nx][ny][w] == 0:
                queue.append((nx, ny, w))
                visited[nx][ny][w] = visited[x][y][w] + 1
    return -1


print(bfs(graph))

from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

visited = [[0] * m for i in range(n)]

queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            queue.append((i, j))
            visited[i][j] = 1

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                if graph[nx][ny] == 1:
                    continue
                elif graph[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
                else:
                    return visited[x][y]
    return -1


result = bfs()
print("NIE" if result == -1 else f"TAK\n{result}")

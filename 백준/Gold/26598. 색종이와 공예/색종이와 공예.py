from collections import deque

n, m = map(int, input().split())

graph = [list(input()) for _ in range(n)]

visited = [[0] * m for _ in range(n)]


def bfs(queue, start):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    ct = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == start and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
                    ct += 1
    return (x, y), ct


st = 0
result = []
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            queue = deque()
            queue.append((i, j))
            start = graph[i][j]
            start_point = (i, j)
            visited[i][j] = 1
            end_point, ct = bfs(queue, start)
            if (end_point[0] - start_point[0] + 1) * (
                end_point[1] - start_point[1] + 1
            ) == ct:
                result.append(True)
            else:
                result.append(False)

print("dd" if all(result) else "BaboBabo")

# BBAA
# BBAA
# CAAA

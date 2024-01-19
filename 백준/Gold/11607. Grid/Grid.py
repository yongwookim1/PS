from collections import deque

n, m = map(int, input().split())

graph = [list(map(int, input())) for _ in range(n)]

queue = deque()
queue.append((0, 0))

visited = [[0] * m for _ in range(n)]
visited[0][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    while queue:
        x, y = queue.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y] - 1
        d = graph[x][y]
        for i in range(4):
            nx = x + (dx[i] * d)
            ny = y + (dy[i] * d)
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    return -1


result = bfs()
if result == -1:
    print("IMPOSSIBLE")
else:
    print(result)

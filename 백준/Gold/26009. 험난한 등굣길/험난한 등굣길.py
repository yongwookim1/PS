from collections import deque

n, m = map(int, input().split())

graph = [[0] * m for _ in range(n)]

t = int(input())

tj = []
for _ in range(t):
    r, c, d = map(int, input().split())
    tj.append((r - 1, c - 1, d))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


for i in tj:
    r, c, d = i
    for i in range(d + 1):
        if 0 <= r + i < n and 0 <= c + (d - i) < m:
            graph[r + i][c + (d - i)] = 1
        if 0 <= r + i < n and 0 <= c - (d - i) < m:
            graph[r + i][c - (d - i)] = 1
        if 0 <= r - i < n and 0 <= c + (d - i) < m:
            graph[r - i][c + (d - i)] = 1
        if 0 <= r - i < n and 0 <= c - (d - i) < m:
            graph[r - i][c - (d - i)] = 1


def bfs(queue, visited):
    while queue:
        y, x = queue.popleft()
        if y == n - 1 and x == m - 1:
            return visited[y][x]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == -1:
                if graph[ny][nx] == 0:
                    visited[ny][nx] = visited[y][x] + 1
                    queue.append((ny, nx))
    return False


queue = deque()
queue.append((0, 0))
visited = [[-1] * m for _ in range(n)]
visited[0][0] = 0
r = bfs(queue, visited)

if r:
    print("YES")
    print(r)
else:
    print("NO")

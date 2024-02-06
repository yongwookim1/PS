from collections import deque

n, m = map(int, input().split())

graph = [list(map(int, input())) for _ in range(n)]

start = []
for i in range(3):
    start.append(tuple(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(queue, visited):
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == -1:
                if graph[ny][nx] == 0:
                    visited[ny][nx] = visited[y][x] + 1
                    queue.append((ny, nx))
    return visited


visited1 = [[-1] * m for _ in range(n)]
visited1[start[0][0] - 1][start[0][1] - 1] = 0
visited2 = [[-1] * m for _ in range(n)]
visited2[start[1][0] - 1][start[1][1] - 1] = 0
visited3 = [[-1] * m for _ in range(n)]
visited3[start[2][0] - 1][start[2][1] - 1] = 0

queue1, queue2, queue3 = deque(), deque(), deque()
queue1.append((start[0][0] - 1, start[0][1] - 1))
queue2.append((start[1][0] - 1, start[1][1] - 1))
queue3.append((start[2][0] - 1, start[2][1] - 1))

visited1 = bfs(queue1, visited1)
visited2 = bfs(queue2, visited2)
visited3 = bfs(queue3, visited3)

r = []
for i in range(n):
    for j in range(m):
        if visited1[i][j] != -1 and visited2[i][j] != -1 and visited3[i][j] != -1:
            r.append(max(visited1[i][j], visited2[i][j], visited3[i][j]))

if r:
    print(min(r))
    print(r.count(min(r)))
else:
    print(-1)

from collections import deque

n, m, k = map(int, input().split())

graph = [list(input()) for _ in range(n)]

x1, x2, e1, e2 = map(int, input().split())

x1, x2, e1, e2 = x1 - 1, x2 - 1, e1 - 1, e2 - 1

queue = deque()
queue.append((x1, x2))

visited = [[float("inf")] * m for _ in range(n)]
visited[x1][x2] = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


while queue:
    y, x = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        nk = 1
        while (
            nk <= k
            and 0 <= nx < m
            and 0 <= ny < n
            and graph[ny][nx] != "#"
            and visited[ny][nx] > visited[y][x]
        ):
            if visited[ny][nx] == float("inf"):
                queue.append((ny, nx))
                visited[ny][nx] = visited[y][x] + 1
            nx += dx[i]
            ny += dy[i]
            nk += 1

if visited[e1][e2] == float("inf"):
    print(-1)
else:
    print(visited[e1][e2])

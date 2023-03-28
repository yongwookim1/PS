from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

ct = 0
def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    dx = [-1, 1, 0, 0, 1, 1, -1 , -1]
    dy = [0, 0, -1 ,1 ,1 ,- 1, 1, -1]
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            ct += 1
            bfs(i, j)

print(ct)
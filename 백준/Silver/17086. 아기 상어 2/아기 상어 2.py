from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

queue = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))

dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]


def bfs(graph, queue):
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            if graph[nx][ny] != 0:
                continue
            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx, ny))


bfs(graph, queue)

m = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] > m:
            m = graph[i][j]

print(max(map(max, graph)) - 1)

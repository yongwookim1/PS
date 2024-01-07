from collections import deque

n, m = map(int,input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            start_point = (i, j)
            graph[i][j] = 1

def bfs():
    queue = deque()
    queue.append(start_point)
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return -1

bfs()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            graph[i][j] = -1
        elif graph[i][j] != 0:
            graph[i][j] -= 1
        if (i, j) == start_point:
            graph[i][j] = 0

for i in graph:
    print(*i)
from collections import deque

n,m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))
queue = deque(())
queue.append((0,0))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            elif graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

bfs()
print(graph[n-1][m-1])
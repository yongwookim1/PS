from collections import deque

def bfs(maps):
    graph = maps
    queue = deque()
    queue.append((0,0))
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    n = len(graph) - 1
    m = len(graph[0]) - 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx > n or ny <= -1 or ny > m:
                continue
            if graph[nx][ny] == 0:
                continue
            elif graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

def solution(maps):
    bfs(maps)
    n = len(maps) - 1
    m = len(maps[0]) - 1
    if maps[n][m] == 1:
        answer = -1
    else:
        answer = maps[n][m]
    return answer
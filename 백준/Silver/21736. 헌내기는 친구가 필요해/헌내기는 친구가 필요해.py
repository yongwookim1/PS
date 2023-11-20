from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(input()))


visited = [[False] * m for _ in range(n)]

queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == "I":
            queue.append((i, j))


def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    st = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue
            elif graph[nx][ny] == "X":
                continue
            elif graph[nx][ny] == "P":
                if visited[nx][ny] == True:
                    continue
                else:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    st += 1
            elif graph[nx][ny] == "O":
                if visited[nx][ny] == True:
                    continue
                else:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
    return st


r = bfs()
print(r if r != 0 else "TT")

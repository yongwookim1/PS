from collections import deque


n, m = map(int, input().split())

graph = [list(input()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def divide(queue):
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == "X":
                    graph[nx][ny] = "O"
                    queue.append((nx, ny))


flag = False
for i in range(n):
    if flag == True:
        break
    for j in range(m):
        if graph[i][j] == "X":
            queue = deque()
            queue.append((i, j))
            graph[i][j] = "O"
            divide(queue)
            flag = True
            break


def root(queue, visited):
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                if graph[nx][ny] == ".":
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
                elif graph[nx][ny] == "X":
                    return visited[x][y]
    return -1


mn = m * n
for i in range(n):
    for j in range(m):
        if graph[i][j] == "O":
            queue = deque()
            queue.append((i, j))
            visited = [[0] * m for _ in range(n)]
            r = root(queue, visited)
            if r > -1:
                if r <= mn:
                    mn = r

print(mn)

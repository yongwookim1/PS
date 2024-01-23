from collections import deque

m, n = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(input()))
    for j in range(m):
        if graph[i][j] == "P":
            start = (i, j)
            graph[i][j] == "."

visited = [[False] * m for _ in range(n)]
visited[start[0]][start[1]] = True

queue = deque()
queue.append(start)
if (
    graph[start[0] - 1][start[1]] == "T"
    or graph[start[0] + 1][start[1]] == "T"
    or graph[start[0]][start[1] - 1] == "T"
    or graph[start[0]][start[1] + 1] == "T"
):
    print(0)
    exit()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    st = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False:
                if graph[nx][ny] == "#":
                    continue
                if (
                    graph[nx - 1][ny] == "T"
                    or graph[nx + 1][ny] == "T"
                    or graph[nx][ny - 1] == "T"
                    or graph[nx][ny + 1] == "T"
                ):
                    if graph[nx][ny] == "G":
                        st += 1
                        visited[nx][ny] = True
                    elif graph[nx][ny] == ".":
                        visited[nx][ny] = True
                else:
                    if graph[nx][ny] == "G":
                        st += 1
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                    elif graph[nx][ny] == ".":
                        visited[nx][ny] = True
                        queue.append((nx, ny))
    return st


print(bfs())

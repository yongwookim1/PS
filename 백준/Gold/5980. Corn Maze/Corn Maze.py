from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(input()))
    for j in range(m):
        if graph[i][j] == "#":
            pass
        elif graph[i][j] == ".":
            pass
        elif graph[i][j] == "=":
            end = (i, j)
        elif graph[i][j] == "@":
            start = (i, j, 0)

queue = deque()
queue.append(start)

visited = [[False] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    while queue:
        x, y, d = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False:
                if graph[nx][ny] == "#":
                    continue
                elif graph[nx][ny] == ".":
                    visited[nx][ny] = True
                    queue.append((nx, ny, d + 1))
                elif graph[nx][ny] == "=":
                    visited[nx][ny] = True
                    return d + 1
                elif graph[nx][ny] == "@":
                    continue
                else:
                    flag = False
                    for p in range(n):
                        if flag:
                            flag = False
                            break
                        for q in range(m):
                            if graph[p][q] == graph[nx][ny] and (p, q) != (nx, ny):
                                queue.append((p, q, d + 1))
                                flag = True
                                break


print(bfs())

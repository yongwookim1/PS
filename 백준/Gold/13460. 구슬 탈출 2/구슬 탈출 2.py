from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(input()))
    for j in range(m):
        if graph[i][j] == "R":
            rx = i
            ry = j
        elif graph[i][j] == "B":
            bx = i
            by = j

queue = deque()
queue.append((rx, ry, bx, by, 1))

visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
visited[rx][ry][bx][by] = True

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def move(x, y, dx, dy):
    ct = 0
    while graph[x + dx][y + dy] != "#" and graph[x][y] != "O":
        x += dx
        y += dy
        ct += 1
    return x, y, ct


def bfs():
    while queue:
        rx, ry, bx, by, d = queue.popleft()
        if d > 10:
            return -1
        for i in range(4):
            nrx, nry, rc = move(rx, ry, dx[i], dy[i])
            nbx, nby, bc = move(bx, by, dx[i], dy[i])
            if graph[nbx][nby] != "O":
                if graph[nrx][nry] == "O":
                    return d
                if nrx == nbx and nry == nby:
                    if rc > bc:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    queue.append((nrx, nry, nbx, nby, d + 1))
    return -1


print(bfs())

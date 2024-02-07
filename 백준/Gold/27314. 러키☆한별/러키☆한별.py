from collections import deque

n, m = map(int, input().split())

graph = []
p = []
ex = []
for i in range(n):
    graph.append(list(input()))
    for j in range(m):
        if graph[i][j] == "P":
            p.append((i, j))
        elif graph[i][j] == "H":
            hb = (i, j)
        elif graph[i][j] == "#":
            ex.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(queue: deque, visited: list):
    r = []
    while queue:
        y, x = queue.popleft()
        if graph[y][x] == "P":
            r.append(visited[y][x])
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == -1:
                if graph[ny][nx] == ".":
                    queue.append((ny, nx))
                    visited[ny][nx] = visited[y][x] + 1
                elif graph[ny][nx] == "P":
                    queue.append((ny, nx))
                    visited[ny][nx] = visited[y][x] + 1
                elif graph[ny][nx] == "H":
                    queue.append((ny, nx))
                    visited[ny][nx] = visited[y][x] + 1
                elif graph[ny][nx] == "#":
                    queue.append((ny, nx))
                    visited[ny][nx] = visited[y][x] + 1
    return r


def hbbfs(queue: deque, visited: list, arrive):
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == -1:
                if graph[ny][nx] == ".":
                    queue.append((ny, nx))
                    visited[ny][nx] = visited[y][x] + 1
                elif graph[ny][nx] == "P":
                    queue.append((ny, nx))
                    visited[ny][nx] = visited[y][x] + 1
                elif graph[ny][nx] == "#" and nx == arrive[1] and ny == arrive[0]:
                    visited[ny][nx] = visited[y][x] + 1
                    return visited[ny][nx]
                elif graph[ny][nx] == "#":
                    queue.append((ny, nx))
                    visited[ny][nx] = visited[y][x] + 1

    return False


mx = -1
for i in ex:
    queue = deque()
    queue.append((hb[0], hb[1]))
    visited = [[-1] * m for _ in range(n)]
    visited[hb[0]][hb[1]] = 0
    hbd = hbbfs(queue, visited, (i[0], i[1]))
    if hbd == False:
        continue
    queue = deque()
    queue.append((i[0], i[1]))
    visited = [[-1] * m for _ in range(n)]
    visited[i[0]][i[1]] = 0
    r = bfs(queue, visited)
    st = 0
    for j in r:
        if j <= hbd:
            st += 1
    mx = max(st, mx)

print(mx)

from collections import deque

r, c = map(int, input().split())

graph = []
for i in range(r):
    graph.append(list(input()))


def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    s = 0
    w = 0
    while queue:
        x, y = queue.popleft()

        if graph[x][y] == "o":
            s += 1
            graph[x][y] = "c"
        elif graph[x][y] == "v":
            w += 1
            graph[x][y] = "c"
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= r or nx < 0 or ny >= c or ny < 0:
                continue
            elif graph[nx][ny] == "o":
                graph[nx][ny] = "c"
                queue.append((nx, ny))
                s += 1
            elif graph[nx][ny] == "v":
                graph[nx][ny] = "c"
                queue.append((nx, ny))
                w += 1
            elif graph[nx][ny] == ".":
                graph[nx][ny] = "c"
                queue.append((nx, ny))
            elif graph[nx][ny] == "#":
                continue

    if s > w:
        return ["sheep", s]
    else:
        return ["wolf", w]


ss = 0
sw = 0
queue = deque()
for i in range(r):
    for j in range(c):
        if graph[i][j] == "o" or graph[i][j] == "v":
            queue.append((i, j))
            win, number = bfs()
            if win == "sheep":
                ss += number
            elif win == "wolf":
                sw += number

print(ss, sw)

from collections import deque

while True:
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break

    graph = []
    graph2 = []
    for i in range(l):
        for j in range(r):
            graph2.append(list(input()))
        graph.append(graph2)
        graph2 = []
        input()
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if graph[i][j][k] == "S":
                    start_point = (i, j, k)
                    graph[i][j][k] = "."
                elif graph[i][j][k] == "E":
                    end_point = (i, j, k)
                    graph[i][j][k] = "."

    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]

    queue = deque()
    queue.append(start_point)

    visited = [[[0] * c for _ in range(r)] for _ in range(l)]
    visited[start_point[0]][start_point[1]][start_point[2]] = 1

    def bfs():
        while queue:
            z, x, y = queue.popleft()
            if z == end_point[0] and x == end_point[1] and y == end_point[2]:
                return visited[z][x][y] - 1
            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]
                if (
                    0 <= nx < r
                    and 0 <= ny < c
                    and 0 <= nz < l
                    and visited[nz][nx][ny] == 0
                ):
                    if graph[nz][nx][ny] == ".":
                        visited[nz][nx][ny] = visited[z][x][y] + 1
                        queue.append((nz, nx, ny))
        return -1

    minute = bfs()
    if minute == -1:
        print("Trapped!")
    else:
        print(f"Escaped in {minute} minute(s).")

from collections import deque

t = int(input())
for _ in range(t):
    m, n = map(int, input().split())

    graph = []
    fire = []
    for i in range(n):
        graph.append(list(input()))
        for j in range(m):
            if graph[i][j] == "@":
                start = (i, j, 0)
            elif graph[i][j] == "*":
                fire.append((i, j))

    sq, fq = deque(), deque()
    sq.append(start)
    for i in fire:
        fq.append(i)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(sq, fq, visited1, visited2):
        sq2, fq2 = deque(), deque()
        while sq:
            while fq:
                x, y = fq.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m and visited1[nx][ny] == False:
                        if graph[nx][ny] == ".":
                            visited1[nx][ny] = True
                            fq2.append((nx, ny))
                            graph[nx][ny] = "*"
            while sq:
                x, y, d = sq.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m and visited2[nx][ny] == False:
                        if graph[nx][ny] == ".":
                            visited2[nx][ny] = True
                            sq2.append((nx, ny, d + 1))
                    elif nx < 0 or nx >= n or ny < 0 or ny >= m:
                        return d + 1
            sq, fq = sq2, fq2
            sq2, fq2 = deque(), deque()
        return -1

    visited1 = [[False] * m for _ in range(n)]
    visited2 = [[False] * m for _ in range(n)]

    result = bfs(sq, fq, visited1, visited2)

    print("IMPOSSIBLE") if result == -1 else print(result)

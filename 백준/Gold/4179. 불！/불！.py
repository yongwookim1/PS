from collections import deque

n, m = map(int, input().split())

graph = []
fire = []
for i in range(n):
    graph.append(list(input()))
    for j in range(m):
        if graph[i][j] == "J":
            jh = (i, j, 0)
            graph[i][j] = "."
        elif graph[i][j] == "F":
            fire.append((i, j))

jq, fq = deque(), deque()
jq.append(jh)
for i in fire:
    fq.append(i)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(jq, fq, visited1, visited2):
    jq2, fq2 = deque(), deque()
    while jq:
        while fq:
            x, y = fq.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and visited2[nx][ny] == False:
                    if graph[nx][ny] == ".":
                        visited2[nx][ny] = True
                        graph[nx][ny] = "F"
                        fq2.append((nx, ny))
                    if graph[nx][ny] == "J":
                        visited2[nx][ny] = True
                        return -1
        while jq:
            x, y, d = jq.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and visited1[nx][ny] == False:
                    if graph[nx][ny] == ".":
                        visited1[nx][ny] = True
                        jq2.append((nx, ny, d + 1))
                elif 0 > nx or nx >= n or 0 > ny or ny >= m:
                    return d + 1
        jq, fq = jq2, fq2
        jq2, fq2 = deque(), deque()

    return -1


visited1 = [[False] * m for _ in range(n)]
visited2 = [[False] * m for _ in range(n)]

r = bfs(jq, fq, visited1, visited2)

if r == -1:
    print("IMPOSSIBLE")
else:
    print(r)

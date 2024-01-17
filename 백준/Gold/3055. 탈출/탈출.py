from collections import deque

n, m = map(int, input().split())

start, water = 0, []

graph = []
for i in range(n):
    graph.append(list(input()))
    for j in range(m):
        if graph[i][j] == "S":
            start = (i, j, 0)
        elif graph[i][j] == "*":
            water.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
queue.append(start)

tq = deque()
for i in water:
    tq.append(i)


def flood(queue, tq, visited1, visited2):
    tq2, queue2 = deque(), deque()
    while queue:
        while tq:
            x, y = tq.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and visited1[nx][ny] == False:
                    if graph[nx][ny] == ".":
                        visited1[nx][ny] = True
                        tq2.append((nx, ny))
                        graph[nx][ny] = "*"

        while queue:
            x, y, d = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and visited2[nx][ny] == False:
                    if graph[nx][ny] == ".":
                        visited2[nx][ny] = True
                        queue2.append((nx, ny, d + 1))
                    elif graph[nx][ny] == "D":
                        return d + 1
        tq, queue = tq2, queue2
        tq2, queue2 = deque(), deque()
    return -1


visited1 = [[False] * m for _ in range(n)]
visited2 = [[False] * m for _ in range(n)]

result = flood(queue, tq, visited1, visited2)

if result == -1:
    print("KAKTUS")
else:
    print(result)

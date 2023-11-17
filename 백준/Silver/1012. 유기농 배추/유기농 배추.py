from collections import deque


def bfs():
    while queue:
        x, y = queue.popleft()
        dx = [-1, 1, 0, 0]
        dy = [0, 0, 1, -1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or ny >= m or nx < 0 or ny < 0:
                continue
            elif graph[nx][ny] == 0:
                continue
            elif graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))


t = int(input())
for i in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    for i in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    queue = deque()
    st = 0
    for i in range(m):
        for j in range(n):
            if graph[j][i] == 1:
                queue.append((j, i))
                bfs()
                st += 1

    print(st)

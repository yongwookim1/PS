from collections import deque


n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

t = int(input())

ng = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(0, m * 3, 3):
        if sum(graph[i][j : j + 3]) >= 3 * t:
            ng[i][j // 3] = 255
        else:
            ng[i][j // 3] = 0


def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue
            elif ng[nx][ny] == 0:
                continue
            elif ng[nx][ny] == 255:
                ng[nx][ny] = 0
                queue.append((nx, ny))


queue = deque()

st = 0
for i in range(n):
    for j in range(m):
        if ng[i][j] == 255:
            queue.append((i, j))
            bfs()
            st += 1
print(st)

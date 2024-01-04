from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

graph2 = []
for i in range(n):
    graph2.append(list(map(int, input().split())))

queue = deque()

flag = False
for i in range(n):
    if flag == True:
        break
    for j in range(m):
        if graph[i][j] != graph2[i][j]:
            queue.append((i, j))
            number = graph[i][j]
            vaccine = graph2[i][j]
            flag = True
            break

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs():
    while queue:
        x, y = queue.popleft()
        graph[x][y] = vaccine
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == number:
                    graph[nx][ny] = vaccine
                    queue.append((nx, ny))


bfs()

if graph == graph2:
    print("YES")
else:
    print("NO")

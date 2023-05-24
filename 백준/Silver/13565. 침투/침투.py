from collections import deque

m, n = map(int, input().split())

graph = []
for _ in range(m):
    graph.append(list(map(int, input())))
electron = []
for i, j in enumerate(graph[0]):
    if j == 0:
        electron.append(i)

queue = deque()
for k in electron:
    queue.append((0, k))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph, queue):
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            if graph[ny][nx] == 1:
                continue
            if graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1
                queue.append((ny, nx))
    return graph


bfs(graph, queue)

for l in graph[-1]:
    if l > 1:
        print("YES")
        break
else:
    print("NO")

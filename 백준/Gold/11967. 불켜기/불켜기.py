from collections import deque

n, m = map(int, input().split())

graph = [[0] * n for _ in range(n)]
graph[0][0] = 1

rooms = dict()
for i in range(m):
    x, y, a, b = map(int, input().split())
    x, y, a, b = x - 1, y - 1, a - 1, b - 1
    try:
        rooms[(x, y)].append((a, b))
    except:
        rooms[(x, y)] = []
        rooms[(x, y)].append((a, b))

st = 1
for x1, x2 in rooms[(0, 0)]:
    if graph[x1][x2] == 0:
        graph[x1][x2] = 1
        st += 1
del rooms[(0, 0)]

queue = deque()
queue.append((0, 0))

visited = [[False] * n for _ in range(n)]
visited[0][0] = True


def bfs(queue, visited, st):
    while queue:
        y, x = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if (
                0 <= nx < n
                and 0 <= ny < n
                and not visited[ny][nx]
                and graph[ny][nx] == 1
            ):
                if (ny, nx) in rooms.keys():
                    for x1, x2 in rooms[(ny, nx)]:
                        if graph[x1][x2] == 0:
                            graph[x1][x2] = 1
                            st += 1
                    queue.append((ny, nx))
                    visited = [[False] * n for _ in range(n)]
                    visited[ny][nx] = True
                    del rooms[(ny, nx)]
                else:
                    queue.append((ny, nx))
                    visited[ny][nx] = True
    return st


print(bfs(queue, visited, st))

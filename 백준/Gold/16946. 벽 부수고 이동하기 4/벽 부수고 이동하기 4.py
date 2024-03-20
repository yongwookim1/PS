from collections import deque

n, m = map(int, input().split())

graph = [list(map(int, input())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]


def bfs(queue, visited, st):
    ct = 0
    while queue:
        y, x = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx]:
                if graph[ny][nx] == 0:
                    graph[ny][nx] = st
                    ct += 1
                    visited[ny][nx] = True
                    queue.append((ny, nx))
    return ct


st = 2
group = dict()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            ct = 1
            graph[i][j] = 2
            queue = deque()
            queue.append((i, j))
            visited[i][j] = True
            graph[i][j] = st
            ct += bfs(queue, visited, st)
            group[st] = ct
            st += 1


def bfs2(queue):
    ct = 0
    s = set()
    while queue:
        y, x = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < m and 0 <= ny < n:
                if graph[ny][nx] == 1:
                    continue
                elif graph[ny][nx] != 1:
                    s.add(graph[ny][nx])
    for i in s:
        ct += group[i]
    return ct


ng = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            ct = 1
            queue = deque()
            queue.append((i, j))
            r = bfs2(queue)
            ct += r
            ct %= 10
            ng[i][j] = ct

for i in ng:
    print(*i, sep="")

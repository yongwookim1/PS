from collections import deque

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]


def bfs(queue, visited):
    ct = 0
    while queue:
        y, x = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx]:
                if graph[ny][nx] == 1:
                    graph[ny][nx] = st
                    ct += 1
                    visited[ny][nx] = True
                    queue.append((ny, nx))
    return ct


st = 2
group = dict()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            ct = 1
            queue = deque()
            queue.append((i, j))
            graph[i][j] = st
            visited[i][j] = True
            ct += bfs(queue, visited)
            group[st] = ct
            st += 1


def bfs2(queue):
    ct = 1
    ad = set()
    while queue:
        y, x = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < m and 0 <= ny < n:
                if graph[ny][nx] != 0:
                    ad.add(graph[ny][nx])
    for i in ad:
        ct += group[i]
    return ct


mx = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            queue = deque()
            queue.append((i, j))
            r = bfs2(queue)
            mx = max(r, mx)

print(mx)

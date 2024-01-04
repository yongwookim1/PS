from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(map, queue, visited):
    p, q = queue[0]
    visited[p][q] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                if map[nx][ny] == "W":
                    continue
                elif map[nx][ny] == "L":
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
    mx = 0
    for i in visited:
        mx = max(max(i) - 1, mx)
    return mx


r = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == "L":
            queue = deque()
            visited_tmp = [[0] * m for _ in range(n)]
            queue.append((i, j))
            r = max(bfs(graph, queue, visited_tmp), r)

print(r)

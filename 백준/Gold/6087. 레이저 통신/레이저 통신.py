from collections import deque

m, n = map(int, input().split())

graph = []
start = deque()
for i in range(n):
    graph.append(list(input()))
    for j in range(m):
        if graph[i][j] == "C":
            start.append((i, j))

queue = deque()
queue.append(start.popleft())

visited = [[float("inf")] * m for _ in range(n)]
visited[queue[0][0]][queue[0][1]] = -1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(queue, visited):
    while queue:
        y, x = queue.popleft()
        if y == start[0][0] and x == start[0][1]:
            return visited[y][x]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            while (
                0 <= nx < m
                and 0 <= ny < n
                and graph[ny][nx] != "*"
                and visited[ny][nx] > visited[y][x]
            ):
                if visited[ny][nx] == float("inf"):
                    visited[ny][nx] = visited[y][x] + 1
                    queue.append((ny, nx))
                nx += dx[i]
                ny += dy[i]


print(bfs(queue, visited))

from collections import deque

graph = [["."] * 8 for _ in range(16)]
graph.extend([list(input()) for _ in range(8)])

queue = deque()
queue.append((23, 0, 0))

visited = [[False] * 8 for _ in range(24)]


dx = [0, -1, 1, 0, -1, 1, 0, -1, 1]
dy = [0, 0, 0, -1, -1, -1, 1, 1, 1]


def bfs(queue, visited):
    while queue:
        y, x, d = queue.popleft()
        if d == 7:
            return 1
        for i in range(9):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 8 and 0 <= ny < 24 and visited[ny][nx] == False:
                if graph[ny][nx] == "." and graph[ny - 1][nx] == ".":
                    if 3 <= i <= 5:
                        queue.append((ny - 1, nx, d + 1))
                    elif 6 <= i <= 8:
                        queue.append((ny - 1, nx, d - 1))
                    else:
                        queue.append((ny - 1, nx, d))
                    visited[ny][nx] = True
    return 0


print(bfs(queue, visited))

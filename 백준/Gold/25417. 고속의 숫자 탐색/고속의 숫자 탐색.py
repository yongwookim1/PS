from collections import deque

graph = [list(map(int, input().split())) for _ in range(5)]

r, c = map(int, input().split())

queue = deque()
queue.append((r, c, 0))

visited = [[False] * 5 for _ in range(5)]
visited[r][c] = True

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(queue, visited):
    while queue:
        y, x, d = queue.popleft()
        if graph[y][x] == 1:
            return d
        for i in range(4):
            rx = x
            ry = y
            while True:
                nx = rx + dx[i]
                ny = ry + dy[i]
                if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                    break
                if graph[ny][nx] == -1:
                    break
                if graph[ny][nx] == 7:
                    ry, rx = ny, nx
                    break
                ry, rx = ny, nx
            if visited[ry][rx]:
                continue
            queue.append((ry, rx, d + 1))
            visited[ry][rx] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                continue
            if graph[ny][nx] == -1:
                continue
            if visited[ny][nx]:
                continue
            queue.append((ny, nx, d + 1))
            visited[ny][nx] = True
    return -1


print(bfs(queue, visited))

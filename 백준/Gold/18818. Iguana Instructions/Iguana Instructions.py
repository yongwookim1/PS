from collections import deque

n = int(input())

graph = [list(input()) for _ in range(n)]

queue = deque()
queue.append((0, 0))

visited = [[float("inf")] * n for _ in range(n)]
visited[0][0] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(queue, vistied):
    while queue:
        y, x = queue.popleft()
        if y == n - 1 and x == n - 1:
            return visited[y][x]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            while (
                0 <= nx < n
                and 0 <= ny < n
                and graph[ny][nx] != "#"
                and visited[ny][nx] > visited[y][x]
            ):
                if visited[ny][nx] == float("inf"):
                    visited[ny][nx] = visited[y][x] + 1
                    queue.append((ny, nx))
                nx += dx[i]
                ny += dy[i]
    return -1


print(bfs(queue, visited))

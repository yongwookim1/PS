from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(queue: deque, visited: list):
    while queue:
        y, x = queue.popleft()
        if y == n - 1 and x == m - 1:
            return visited[y][x]
        if graph[y][x] == "+":
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == -1:
                    if graph[ny][nx] != "*":
                        visited[ny][nx] = visited[y][x] + 1
                        queue.append((ny, nx))
        elif graph[y][x] == "-":
            for i in range(2):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == -1:
                    if graph[ny][nx] != "*":
                        visited[ny][nx] = visited[y][x] + 1
                        queue.append((ny, nx))
        elif graph[y][x] == "|":
            for i in range(2, 4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == -1:
                    if graph[ny][nx] != "*":
                        visited[ny][nx] = visited[y][x] + 1
                        queue.append((ny, nx))
    return -1


for _ in range(int(input())):
    n = int(input())
    m = int(input())
    graph = [list(input()) for _ in range(n)]

    queue = deque()
    queue.append((0, 0))
    visited = [[-1] * m for _ in range(n)]
    visited[0][0] = 1

    print(bfs(queue, visited))

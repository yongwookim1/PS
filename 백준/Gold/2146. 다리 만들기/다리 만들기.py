from collections import deque

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

nb = 2


def numbering(queue: deque, nb: int):
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = nb
                    queue.append((nx, ny))


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            queue = deque()
            queue.append((i, j))
            graph[i][j] = nb
            numbering(queue, nb)
            nb += 1


def building(queue: deque, visited: list, start_number: int):
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
                elif graph[nx][ny] != start_number:
                    return visited[x][y]
    return 0


mn = float("inf")
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            start_number = graph[i][j]
            queue = deque()
            queue.append((i, j))
            visited = [[0] * n for _ in range(n)]
            r = building(queue, visited, start_number)
            if r:
                mn = min(mn, r)

print(mn)

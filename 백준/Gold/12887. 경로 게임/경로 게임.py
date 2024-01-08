from collections import deque
import copy

n = int(input())

graph = []
for i in range(2):
    graph.append(list(input()))


def bfs(queue, visited):
    dx = [-1, 1, 0]
    dy = [0, 0, 1]
    while queue:
        x, y = queue.popleft()
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 2 and 0 <= ny < n and visited[nx][ny] == 0:
                if graph[nx][ny] == ".":
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
    return visited


def search(start_point):
    queue = deque()
    queue.append(start_point)
    p, q = start_point
    visited = [[0] * n for _ in range(2)]
    visited[p][q] = 1

    bfs(queue, visited)

    if visited[0][n - 1] == 0:
        end_point = visited[1][n - 1]
    elif visited[1][n - 1] == 0:
        end_point = visited[0][n - 1]
    else:
        end_point = min(visited[0][n - 1], visited[1][n - 1])

    st = 0
    for i in range(2):
        for j in range(n):
            if graph[i][j] == "#":
                st += 1
    return (2 * n) - st - end_point


if graph[0][0] == "#" and graph[1][0] == ".":
    print(search((1, 0)))
elif graph[0][0] == "." and graph[1][0] == "#":
    print(search((0, 0)))
else:
    print(max(search((0, 0)), search((1, 0))))

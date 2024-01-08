from collections import deque
import sys

input = sys.stdin.readline

n = int(input().rstrip())

graph = []
for i in range(n):
    graph.append(list(input().rstrip()))
    for j in range(n):
        if graph[i][j] == "F":
            start_point = (i, j)


dx = [-1, 0, 0, 1, -1, 1, -1]
dy = [0, -1, 1, 1, -1, -1, 1]


def bfs(queue, visited):
    while queue:
        x, y = queue.popleft()
        for i in range(7):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
                if graph[nx][ny] == ".":
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                elif graph[nx][ny] == "F":
                    return True
    return False


st = 0
queue = deque()
queue.append(start_point)
visited = [[False] * n for _ in range(n)]
p, q = start_point
visited[p][q] = True
bfs(queue, visited)

st = -1
for i in range(n):
    for j in range(n):
        if visited[i][j]:
            st += 1

sys.stdout.write(str(st))

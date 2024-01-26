from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().strip().split())) for _ in range(n)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, 1, -1, -1, 0, 1]

visited1 = [[False] * m for _ in range(n)]


def bfs(queue, visited1, visited2, h):
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited2[nx][ny] == False:
                if graph[nx][ny] > h:
                    return 0
                elif graph[nx][ny] == h:
                    visited1[nx][ny] = True
                    visited2[nx][ny] = True
                    queue.append((nx, ny))
                elif graph[nx][ny] == h - 1:
                    continue
    return 1


st = 0
for i in range(n):
    for j in range(m):
        if visited1[i][j] == False and graph[i][j] != 0:
            queue = deque()
            queue.append((i, j))
            visited1[i][j] = True
            visited2 = [[False] * m for _ in range(n)]
            visited2[i][j] = True
            st += bfs(queue, visited1, visited2, graph[i][j])
print(st)

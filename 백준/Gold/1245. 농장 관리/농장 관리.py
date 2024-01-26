from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().strip().split())) for _ in range(n)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, 1, -1, -1, 0, 1]


def bfs(queue, h):
    r = 1
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == h and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                elif graph[nx][ny] > h:
                    r = 0
    return r


visited = [[False] * m for _ in range(n)]
st = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] != 0 and visited[i][j] == False:
            queue = deque()
            queue.append((i, j))
            visited[i][j] = True
            st += bfs(queue, graph[i][j])

print(st)

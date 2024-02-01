from collections import deque
import sys

input = sys.stdin.readline

k = int(input())

m, n = map(int, input().strip().split())

graph = [list(map(int, input().strip().split())) for _ in range(n)]

queue = deque()
queue.append((0, 0, 0))

visited = [[[-1] * (k + 1) for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

hx = [2, 2, -2, -2, 1, 1, -1, -1]
hy = [1, -1, 1, -1, 2, -2, 2, -2]


def bfs(queue: deque, visited: list):
    while queue:
        x, y, h = queue.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][h]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny][h] == -1:
                if graph[nx][ny] == 0:
                    visited[nx][ny][h] = visited[x][y][h] + 1
                    queue.append((nx, ny, h))
        if h < k:
            for i in range(8):
                nx = x + hx[i]
                ny = y + hy[i]
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny][h + 1] == -1:
                    if graph[nx][ny] == 0:
                        visited[nx][ny][h + 1] = visited[x][y][h] + 1
                        queue.append((nx, ny, h + 1))
    return -1


print(bfs(queue, visited))

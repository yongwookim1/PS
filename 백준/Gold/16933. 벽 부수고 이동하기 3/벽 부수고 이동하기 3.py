from collections import deque
import sys

input = sys.stdin.readline

n, m, k = map(int, input().rstrip().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().rstrip())))

visited = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]
visited[0][0][k] = 1

queue = deque()
queue.append((0, 0, k, 0, 1))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs():
    while queue:
        x, y, k, t, d = queue.popleft()
        if x == n - 1 and y == m - 1:
            return d
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and visited[nx][ny][k] == 0:
                    visited[nx][ny][k] = 1
                    queue.append((nx, ny, k, 1 - t, d + 1))
                elif graph[nx][ny] == 1 and k > 0 and visited[nx][ny][k - 1] == 0:
                    # breaking the wall right away
                    if t == 0:
                        visited[nx][ny][k - 1] = 1
                        queue.append((nx, ny, k - 1, 1 - t, d + 1))
                    # waiting for the daytime
                    elif t == 1:
                        queue.append((x, y, k, 1 - t, d + 1))

    return -1


sys.stdout.write(str(bfs()))

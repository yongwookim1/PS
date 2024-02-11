from collections import deque
import sys

input = sys.stdin.readline
n, m, k = map(int, input().rstrip().split())

graph = []
mq = deque()
for i in range(n):
    tmp_graph = list(map(int, input().rstrip().split()))
    for j in range(m):
        if tmp_graph[j] == 3:
            mq.append((i, j, 0))
        elif tmp_graph[j] == 4:
            start = (i, j, 0)
    graph.append(tmp_graph)

visited = [[False] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def obstacle(queue):
    while queue:
        y, x, d = queue.popleft()
        visited[y][x] = True
        if d == k:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == False:
                visited[ny][nx] = True
                queue.append((ny, nx, d + 1))


def bfs(queue, visited):
    while queue:
        y, x, d = queue.popleft()
        if graph[y][x] == 2:
            return d
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == False:
                if graph[ny][nx] == 0:
                    visited[ny][nx] = True
                    queue.append((ny, nx, d + 1))
                elif graph[ny][nx] == 2:
                    visited[ny][nx] = True
                    queue.append((ny, nx, d + 1))
    return -1


queue = deque()
queue.append(start)
obstacle(mq)
print(bfs(queue, visited))

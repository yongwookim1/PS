from collections import deque
import sys
from copy import deepcopy

input = sys.stdin.readline

n, m = map(int, input().strip().split())

graph = []
queue = deque()

for i in range(n):
    graph.append(list(input().strip()))
    for j in range(m):
        if graph[i][j] == ".":
            queue.append((i, j))

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]


def bfs(queue):
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False:
                if graph[nx][ny] == ".":
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                else:
                    st = 0
                    for j in range(8):
                        if graph[nx + dx[j]][ny + dy[j]] == ".":
                            st += 1
                    if st >= int(graph[nx][ny]):
                        visited[nx][ny] = True
                        tq.append((nx, ny))
    if not tq:
        return False
    else:
        for i, j in tq:
            graph[i][j] = "."
    return True


visited = [[False] * m for _ in range(n)]

st = 0
tq = deque()
while True:
    if bfs(queue):
        queue = tq
        tq = deque()
        st += 1
    else:
        break

print(st)

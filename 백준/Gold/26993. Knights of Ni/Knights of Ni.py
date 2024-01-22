from collections import deque
import sys

input = sys.stdin.readline

m, n = map(int, input().split())

graph = []
sh = []
mm = m // 40 + 1
for i in range(n):
    tmp_graph = []
    for j in range(mm):
        tmp_graph.extend(list(map(int, input().strip().split())))
    graph.append(tmp_graph)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            start = (i, j, 0)
            graph[i][j] = 0
        elif graph[i][j] == 3:
            end = (i, j, 1)

queue = deque()
queue.append(start)

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[start[0]][start[1]][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(queue, visited):
    while queue:
        x, y, s = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny][s] == 0:
                if graph[nx][ny] == 0:
                    visited[nx][ny][s] = visited[x][y][s] + 1
                    queue.append((nx, ny, s))
                elif graph[nx][ny] == 3:
                    if s == 0:
                        continue
                    else:
                        return visited[x][y][s]
                elif graph[nx][ny] == 4:
                    visited[nx][ny][1] = visited[x][y][s] + 1
                    queue.append((nx, ny, 1))


print(bfs(queue, visited))

from collections import deque

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

h, w, s1, s2, e1, e2 = map(int, input().split())

queue = deque()
queue.append((s1 - 1, s2 - 1))

visited = [[-1] * m for _ in range(n)]
visited[s1 - 1][s2 - 1] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(queue, visited):
    while queue:
        x, y = queue.popleft()
        if x == e1 - 1 and y == e2 - 1:
            return visited[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < n
                and 0 <= ny < m
                and 0 <= nx + h - 1 < n
                and 0 <= ny + w - 1 < m
                and visited[nx][ny] == -1
            ):
                flag = False
                if i == 0:
                    for j in range(w):
                        if graph[nx][ny + j] == 1:
                            flag = True
                            break
                elif i == 1:
                    for j in range(w):
                        if graph[nx + h - 1][ny + j] == 1:
                            flag = True
                            break
                elif i == 2:
                    for j in range(h):
                        if graph[nx + j][ny] == 1:
                            flag = True
                            break
                else:
                    for j in range(h):
                        if graph[nx + j][ny + w - 1] == 1:
                            flag = True
                            break
                if flag == False:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
    return -1


print(bfs(queue, visited))

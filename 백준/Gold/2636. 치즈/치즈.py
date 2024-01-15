from collections import deque
import time

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(queue, visited):
    queue2 = deque()
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                elif graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue2.append((nx, ny))

    for x, y in queue2:
        graph[x][y] = 0

    return queue2


queue = deque()
queue.append((0, 0))
t = 0
while True:
    result = [element for sublist in graph for element in sublist]
    if all(element == 0 for element in result):
        print(t)
        print(len_left_cheeze)
        break

    visited = [[False] * m for _ in range(n)]
    left_cheeze = [element for sublist in graph for element in sublist]
    len_left_cheeze = len([i for i in left_cheeze if i == 1])
    queue = bfs(queue, visited)
    t += 1

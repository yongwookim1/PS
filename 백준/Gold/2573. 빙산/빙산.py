from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

graph = []
ice = []
for i in range(n):
    graph.append(list(map(int, input().rstrip().split())))
    for j in range(m):
        if graph[i][j] >= 1:
            ice.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q, tq = deque(), deque()


def bfs():
    while q:
        x, y = q.popleft()
        st = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    st += 1
        tq.append((x, y, st))


def melt():
    while tq:
        x, y, st = tq.popleft()
        if graph[x][y] - st <= 0:
            graph[x][y] = 0
        else:
            graph[x][y] -= st


def check(queue, visited):
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False:
                if graph[nx][ny] >= 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny))


ct = 0
flag = False
while True:
    st = 0
    visited = [[False] * m for _ in range(n)]
    mt = []
    for i, j in ice:
        if graph[i][j] >= 1 and visited[i][j] == False:
            queue = deque()
            queue.append((i, j))
            visited[i][j] = True
            check(queue, visited)
            st += 1
            if st >= 2:
                flag = True
                break
        if graph[i][j] == 0:
            mt.append(True)
        else:
            mt.append(False)
    if all(mt):
        print(0)
        break
    if flag == True:
        print(ct)
        break

    visited = [[False] * m for _ in range(n)]
    for i, j in ice:
        if graph[i][j] >= 1:
            q.append((i, j))
            bfs()
    melt()
    ct += 1

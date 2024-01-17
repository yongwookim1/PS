from collections import deque

n, m = map(int, input().split())

r, c, d = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

queue = deque()
queue.append((r, c, d))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs():
    st = 0
    while queue:
        x, y, d = queue.popleft()
        dirty = 0
        if visited[x][y] == False:
            visited[x][y] = True
            st += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == False and graph[nx][ny] == 0:
                    dirty += 1
        if dirty >= 1:
            while True:
                d = (d - 1) % 4
                if (
                    visited[x + dx[d]][y + dy[d]] == False
                    and graph[x + dx[d]][y + dy[d]] == 0
                ):
                    queue.append((x + dx[d], y + dy[d], d))
                    break
        else:
            nd = (d - 2) % 4
            if graph[x + dx[nd]][y + dy[nd]] == 0:
                queue.append((x + dx[nd], y + dy[nd], d))
            else:
                return st


print(bfs())

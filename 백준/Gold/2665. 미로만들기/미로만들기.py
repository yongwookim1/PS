from collections import deque

n = int(input())

graph = [list(map(int, input())) for _ in range(n)]
if n == 1:
    print(0)
    exit()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(queue, visited, st):
    while queue:
        x, y, k = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny][k] == 0:
                if graph[nx][ny] == 1:
                    visited[nx][ny][k] = visited[x][y][k] + 1
                    queue.append((nx, ny, k))
                elif graph[nx][ny] == 0 and k - 1 >= 0:
                    visited[nx][ny][k - 1] = visited[x][y][k] + 1
                    queue.append((nx, ny, k - 1))
                    st -= 1
                if nx == n - 1 and ny == n - 1:
                    return True
    return False


def bfs2(queue, visited):
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if graph[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
                if nx == n - 1 and ny == n - 1:
                    return True
    return False


queue = deque()
queue.append((0, 0))
visited = [[0] * n for _ in range(n)]
if bfs2(queue, visited):
    print(0)
    exit()

for i in range(1, (n * n) + 1):
    queue = deque()
    queue.append((0, 0, i))
    visited = [[[0] * (i + 1) for _ in range(n)] for _ in range(n)]
    r = bfs(queue, visited, i)
    if r:
        print(i)
        break

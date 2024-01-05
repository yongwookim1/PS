from collections import deque

n, m, a, b, k = map(int, input().split())

graph = [[0] * m for _ in range(n)]
for _ in range(k):
    p, q = map(int, input().split())
    graph[p - 1][q - 1] = 1

visited = [[0] * m for _ in range(n)]
start1, start2 = map(int, input().split())
end1, end2 = map(int, input().split())


queue = deque()
queue.append((start1 - 1, start2 - 1))


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs():
    while queue:
        x, y = queue.popleft()
        if x == end1 - 1 and y == end2 - 1:
            return visited[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n - (a - 1) and 0 <= ny < m - (b - 1) and visited[nx][ny] == 0:
                if all(
                    [graph[nx + p][ny + q] == 0 for p in range(a) for q in range(b)]
                ):
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
    return -1


print(bfs())

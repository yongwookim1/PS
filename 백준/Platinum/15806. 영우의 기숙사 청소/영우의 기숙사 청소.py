from collections import deque
import sys

input = sys.stdin.readline

n, m, k, t = map(int, input().strip().split())

graph = [[0] * n for _ in range(n)]
visited = [[[False] * 2 for _ in range(n)] for _ in range(n)]

mold = deque()
for i in range(m):
    p, q = map(int, input().strip().split())
    mold.append((p - 1, q - 1, 0))


check = []
for i in range(k):
    p, q = map(int, input().split())
    check.append((p - 1, q - 1))

dx = [2, 2, 1, 1, -1, -1, -2, -2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]


def increase(queue):
    while queue:
        x, y, d = queue.popleft()
        if d == t:
            break
        day = (d + 1) % 2
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny][day] == False:
                if graph[nx][ny] == 0:
                    visited[nx][ny][day] = True
                    queue.append((nx, ny, d + 1))


increase(mold)

for p, q in check:
    if visited[p][q][t % 2] == 1:
        print("YES")
        break
else:
    print("NO")

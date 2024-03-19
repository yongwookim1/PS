from collections import deque
import sys

input = sys.stdin.readline

n, m, k = map(int, input().rstrip().split())

graph = []
for i in range(n):
    graph.append(list(input().rstrip()))
    for j in range(m):
        if graph[i][j] == "S":
            start1, start2 = i, j
            graph[i][j] = "0"
queue = deque()
queue.append((start1, start2, 0, 4, deque()))

visited = [[[False] * 4 for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(queue: deque, visited: list):
    while queue:
        y, x, t, d, dq = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if d == 4:
                pass
            elif d % 2 == 0:
                if i == d + 1:
                    continue
            elif d % 2 == 1:
                if i == d - 1:
                    continue
            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx][i]:
                if graph[ny][nx] == "H":
                    return t + 1
                if graph[ny][nx] == "X":
                    continue
                tmp_dq = deque()
                tmp_dq.extend(dq)
                if len(dq) < 3:
                    dq.append(int(graph[ny][nx]))
                elif len(dq) >= 3:
                    dq.popleft()
                    dq.append(int(graph[ny][nx]))
                if sum(dq) <= k:
                    visited[ny][nx][i] = True
                    queue.append((ny, nx, t + 1, i, dq))
                dq = tmp_dq
    return -1


print(bfs(queue, visited))

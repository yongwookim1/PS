from collections import deque
from copy import deepcopy

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(input()))

visited = [[0] * m for i in range(n)]

my_queue = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(map, queue, visited):
    p, q = queue[0]
    while queue:
        x, y = queue.popleft()
        if map[x][y] == "W":
            return 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < n
                and 0 <= ny < m
                and visited[nx][ny] == 0
                and (nx != p or ny != q)
            ):
                if map[nx][ny] == "W":
                    continue
                elif map[nx][ny] == "L":
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
    mx = 0
    for i in visited:
        mx = max(max(i), mx)
    return mx


r = 0
for i in range(n):
    for j in range(m):
        graph_tmp = deepcopy(graph)
        queue_tmp = deepcopy(my_queue)
        visited_tmp = deepcopy(visited)
        queue_tmp.append((i, j))
        r = max(bfs(graph_tmp, queue_tmp, visited_tmp), r)

print(r)

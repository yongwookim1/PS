from collections import deque
from itertools import combinations

n, m = map(int, input().split())

graph = []
virus = []
st = 0
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] == 2:
            virus.append((i, j))
        elif graph[i][j] == 0:
            st += 1

if st == 0:
    print(0)
    exit()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(queue):
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 0 or graph[nx][ny] == 2:
                    if visited[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx, ny))
                    elif visited[nx][ny] >= 1:
                        if visited[x][y] + 1 < visited[nx][ny]:
                            visited[nx][ny] = visited[x][y] + 1
                            queue.append((nx, ny))


result = []
for i in combinations(virus, m):
    visited = [[0] * n for _ in range(n)]
    for j in i:
        queue = deque()
        queue.append(j)
        visited[j[0]][j[1]] = 1
        bfs(queue)

    mx = -1
    flag = False
    for i in range(n):
        if flag:
            break
        for j in range(n):
            if visited[i][j] == 0 and graph[i][j] != 1:
                flag = True
            elif visited[i][j] > mx and graph[i][j] != 2:
                mx = visited[i][j]
    if not flag:
        result.append(mx - 1)

if result:
    print(min(result))
else:
    print(-1)

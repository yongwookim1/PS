from collections import deque

n, k = map(int, input().split())

graph = [list(map(int, input())) for _ in range(n)]


def disappear(queue, visited, color):
    ct = 1
    flag = False
    tq = deque()
    tq.append(queue[0])
    while queue:
        y, x = queue.popleft()
        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 10 and 0 <= ny < n and not visited[ny][nx]:
                if graph[ny][nx] == color:
                    visited[ny][nx] = True
                    queue.append((ny, nx))
                    tq.append((ny, nx))
                    ct += 1
    if ct >= k:
        for i, j in tq:
            graph[i][j] = 0
        flag = True
    return flag


def fall():
    for i in range(10):
        st = 0
        for j in range(n - 1, -1, -1):
            if graph[j][i] == 0:
                st += 1
            elif graph[j][i] != 0:
                graph[j][i], graph[j + st][i] = 0, graph[j][i]


while True:
    flag = False
    for i in range(n):
        for j in range(10):
            if graph[i][j] != 0:
                queue = deque()
                queue.append((i, j))
                visited = [[False] * 10 for _ in range(n)]
                visited[i][j] = True
                r = disappear(queue, visited, graph[i][j])
                if not r:
                    continue
                else:
                    flag = True
    if not flag:
        for i in graph:
            print(*i, sep="")
        break
    else:
        fall()

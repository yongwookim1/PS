from collections import deque

n = int(input())

graph = []
queue = deque()
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] == 9:
            queue.append((i, j, 0, 2, 0))
            graph[i][j] = 0
            break

dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]


def bfs(queue: deque, visited: list):
    flag = False
    tq = deque()
    while queue:
        y, x, t, l, eat = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] == False:
                if graph[ny][nx] == 0:
                    visited[ny][nx] = True
                    queue.append((ny, nx, t + 1, l, eat))
                elif graph[ny][nx] < l:
                    if eat + 1 < l:
                        tq.append((ny, nx, t + 1, l, eat + 1))
                    elif eat + 1 == l:
                        tq.append((ny, nx, t + 1, l + 1, 0))
                    result = t + 1
                    flag = True
                elif graph[ny][nx] == l:
                    visited[ny][nx] = True
                    queue.append((ny, nx, t + 1, l, eat))
    if flag:
        return tq
    else:
        return False


res = 0
while True:
    visited = [[False] * n for _ in range(n)]
    visited[queue[0][0]][queue[0][1]] = True
    r = bfs(queue, visited)
    if r == False:
        print(res)
        break
    else:
        tq = r
        tq = list(tq)
        tq.sort(key=lambda x: [x[2], x[0], x[1]])
        queue.append(tq[0])
        graph[queue[0][0]][queue[0][1]] = 0
        res = queue[0][2]

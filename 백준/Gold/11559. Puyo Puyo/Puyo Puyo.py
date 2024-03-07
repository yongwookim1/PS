from collections import deque

graph = [list(input()) for _ in range(12)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def burst(queue: deque, visited: list, alphabet: str):
    ct = 1
    flag = False
    rq = deque()
    rq.append(queue[0])
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 6 and 0 <= ny < 12 and visited[ny][nx] == False:
                if graph[ny][nx] == alphabet:
                    visited[ny][nx] = True
                    queue.append((ny, nx))
                    rq.append((ny, nx))
                    ct += 1
    if ct >= 4:
        for i, j in rq:
            graph[i][j] = "."
        flag = True
    return flag


def let_down():
    for i in range(6):
        st = 0
        for j in range(11, -1, -1):
            if graph[j][i] == ".":
                st += 1
            else:
                d = graph[j][i]
                graph[j][i] = "."
                graph[j + st][i] = d


st = 0
while True:
    flag = False
    for i in range(12):
        for j in range(6):
            if graph[i][j] != ".":
                queue = deque()
                queue.append((i, j))
                visited = [[False] * 6 for _ in range(12)]
                visited[i][j] = True
                alphabet = graph[i][j]
                r = burst(queue, visited, alphabet)
                if r:
                    flag = True
    if flag:
        let_down()
        st += 1
    else:
        break

print(st)

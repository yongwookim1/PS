from collections import deque

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

st = 0
while True:
    result = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                result.append(True)
            else:
                result.append(False)
                break
    if all(result):
        print(st)
        break

    def find_the_hole(queue, graph):
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                    graph[nx][ny] = 2
                    queue.append((nx, ny))

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                queue = deque()
                queue.append((i, j))
                graph[i][j] = 2
                find_the_hole(queue, graph)

    # boundary
    queue = deque()
    queue.append((0, 0))
    graph[0][0] = 2
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 2:
                graph[nx][ny] = 0
                queue.append((nx, ny))

    gone = []

    def bfs(graph, queue):
        while queue:
            x, y = queue.popleft()
            st = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if graph[nx][ny] == 0:
                        st += 1
            if st >= 2:
                gone.append((x, y))

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                queue = deque()
                queue.append((i, j))
                bfs(graph, queue)

    for p, q in gone:
        graph[p][q] = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                graph[i][j] = 0

    st += 1

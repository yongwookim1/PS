from collections import deque

for i in range(int(input())):
    n, m = map(int, input().split())

    queue = deque()
    graph = []
    for i in range(n):
        graph.append(list(input()))
        
    for i in range(n):
        for j in range(m):
            if graph[i][j] == "#":
                graph[i][j] = 1
            else:
                graph[i][j] = 0

    def bfs(graph, queue):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                    continue
                if graph[nx][ny] == 0:
                    continue
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))

    st = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                queue.append((i, j))
                bfs(graph, queue)
                st += 1
    print(st)
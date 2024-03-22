from collections import deque


def bfs(queue: deque, visited: list, doc: list):
    while queue:
        y, x = queue.popleft()
        if 0 <= x < m and 0 <= y < n and not visited[y][x]:
            if graph[y][x] == ".":
                visited[y][x] = True
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx = x + dx
                    ny = y + dy
                    queue.append((ny, nx))
            elif graph[y][x] == "*":
                continue
            elif graph[y][x] == "$":
                visited[y][x] = True
                graph[y][x] = "."
                doc.append(1)
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx = x + dx
                    ny = y + dy
                    queue.append((ny, nx))
            elif graph[y][x].isupper():
                if graph[y][x].lower() in keys:
                    visited[y][x] = True
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx = x + dx
                        ny = y + dy
                        queue.append((ny, nx))
                elif graph[y][x].lower() not in keys:
                    tq.append((y, x))
            elif graph[y][x].islower():
                visited[y][x] = True
                keys.add(graph[y][x])
                graph[y][x] = "."
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx = x + dx
                    ny = y + dy
                    queue.append((ny, nx))


for _ in range(int(input())):
    n, m = map(int, input().split())

    graph = [list(input()) for _ in range(n)]

    keys = set(input())
    doc = []
    tq = deque()

    visited = [[False] * m for _ in range(n)]
    queue = deque()
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                if graph[i][j] != "*":
                    queue.append((i, j))
                    bfs(queue, visited, doc)

    tql = []
    while tq:
        if list(tq) in tql:
            break
        tql.append(list(tq))
        l = len(tq)
        for _ in range(l):
            queue = deque()
            queue.append(tq.popleft())
            bfs(queue, visited, doc)
    print(len(doc))

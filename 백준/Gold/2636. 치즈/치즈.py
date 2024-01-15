from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

graph = [list(map(int, input().rstrip().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time = 0
while True:
    result = [element for sublist in graph for element in sublist]
    if all(element == 0 for element in result):
        print(time)
        print(left_cheeze)
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

    gone = []

    def bfs(queue, graph):
        st = 0
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                    st += 1
                    break
            if st >= 1:
                gone.append((x, y))

    queue = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                queue.append((i, j))
                find_the_hole(queue, graph)

    queue.append((0, 0))
    graph[0][0] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 2:
                graph[nx][ny] = 0
                queue.append((nx, ny))

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                queue.append((i, j))
                bfs(queue, graph)

    left_cheeze_list = [element for sublist in graph for element in sublist]
    left_cheeze = len([True for element in left_cheeze_list if element == 1])

    for p, q in gone:
        graph[p][q] = 0

    time += 1

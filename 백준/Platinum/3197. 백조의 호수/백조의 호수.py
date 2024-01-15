from collections import deque
import sys
import copy

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

swan = []
graph = []
sq, wq, sq_t, wq_t = deque(), deque(), deque(), deque()
for i in range(n):
    graph.append(list(input().rstrip()))
    for j in range(m):
        if graph[i][j] == "L":
            swan.append((i, j))
            wq.append((i, j))
            graph[i][j] = 0
        elif graph[i][j] == ".":
            wq.append((i, j))
            graph[i][j] = 0
        elif graph[i][j] == "X":
            graph[i][j] = 1

sr, sc = swan[0]
er, ec = swan[1]
swan_visited = [[0] * m for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def find_swan():
    while sq:
        x, y = sq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx == er and ny == ec:
                return False
            if 0 <= nx < n and 0 <= ny < m and swan_visited[nx][ny] == 0:
                if graph[nx][ny] == 0:
                    swan_visited[nx][ny] = 1
                    sq.append((nx, ny))
                elif graph[nx][ny] == 1:
                    swan_visited[nx][ny] = 1
                    sq_t.append((nx, ny))
    return True


def melt_down():
    while wq:
        x, y = wq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and swan_visited[nx][ny] == 0:
                if graph[nx][ny] == 1:
                    wq_t.append((nx, ny))
                    graph[nx][ny] = 0


swan_visited[sr][sc] = 1
sq.append((sr, sc))
t = 0

while find_swan():
    t += 1
    melt_down()
    sq, wq = sq_t, wq_t
    sq_t, wq_t = deque(), deque()

print(t)

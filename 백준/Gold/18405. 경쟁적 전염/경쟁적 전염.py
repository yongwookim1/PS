from collections import deque
import sys

input = sys.stdin.readline

n, k = map(int, input().rstrip().split())

graph = [list(map(int, input().rstrip().split())) for _ in range(n)]

s, p, q = map(int, input().rstrip().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(queue):
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y]
                    new[nx][ny] = True
                elif graph[x][y] < graph[nx][ny] and new[nx][ny] == True:
                    graph[nx][ny] = graph[x][y]


for _ in range(s):
    queue = deque()
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                queue.append(((i, j)))
            if graph[p - 1][q - 1] != 0:
                sys.stdout.write(str(graph[p - 1][q - 1]))
                exit()
    new = [[False] * n for _ in range(n)]
    bfs(queue)


sys.stdout.write(str(graph[p - 1][q - 1]))

from collections import deque

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def bfs():
    visited = [[[[0] * m for _ in range(n)] for _ in range(5)] for _ in range(3)]
    dq = deque([(*start, 0, 0, 4)])
    while dq:
        y, x, t, bit, d = dq.popleft()
        if visited[bit][d][y][x]:
            continue
        visited[bit][d][y][x] = 1
        if type(board[y][x]) == int:
            bit |= 1 << board[y][x]
        if bit == 3:
            return t
        for i in range(4):
            if i == d:
                continue
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and board[ny][nx] != "#":
                dq.append((ny, nx, t + 1, bit, i))
    return -1


n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

c = 0
for y in range(n):
    for x in range(m):
        if board[y][x] == "S":
            start = (y, x)
        if board[y][x] == "C":
            board[y][x] = c
            c += 1
print(bfs())

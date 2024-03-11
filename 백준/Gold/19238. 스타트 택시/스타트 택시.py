from collections import deque

n, m, f = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

s1, s2 = map(int, input().split())

start_end = dict()
for _ in range(m):
    sp1, sp2, ep1, ep2 = map(int, input().split())
    start_end[(sp1 - 1, sp2 - 1)] = ep1 - 1, ep2 - 1

queue = deque()
queue.append((s1 - 1, s2 - 1, 0, f))


def go_to_sp(queue: deque, visited: list):
    tq = deque()
    lim = 500000
    while queue:
        y, x, d, f = queue.popleft()
        for dx, dy in [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < n
                and 0 <= ny < n
                and visited[ny][nx] == False
                and f > 0
                and d <= lim
            ):
                visited[ny][nx] = True
                if dx == 0 and dy == 0:
                    if graph[ny][nx] == 0 and (ny, nx) in start_end.keys():
                        queue.append((ny, nx, d, f))
                        tq.append((ny, nx, d, f, 0))
                        lim = d + 1
                    elif graph[ny][nx] == 0:
                        queue.append((ny, nx, d, f))
                else:
                    if graph[ny][nx] == 0 and (ny, nx) in start_end.keys():
                        queue.append((ny, nx, d + 1, f - 1))
                        tq.append((ny, nx, d + 1, f - 1, 0))
                        lim = d + 1
                    elif graph[ny][nx] == 0:
                        queue.append((ny, nx, d + 1, f - 1))

    if tq:
        tq = sorted(tq, key=lambda x: [x[2], x[0], x[1]])
        queue = deque()
        queue.append(tq[0])
        ep = start_end[(queue[0][0], queue[0][1])]
        del start_end[(queue[0][0], queue[0][1])]
        return queue, ep
    else:
        return False


def go_to_ep(queue: deque, visited: list, ep: tuple):
    while queue:
        y, x, d, f, af = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] == False and f > 0:
                visited[ny][nx] = True
                if graph[ny][nx] == 0 and ep == (ny, nx):
                    queue = deque()
                    queue.append((ny, nx, d + 1, f - 1 + ((af + 1) * 2)))
                    return queue
                elif graph[ny][nx] == 0:
                    queue.append((ny, nx, d + 1, f - 1, af + 1))
    return False


while True:
    visited = [[False] * n for _ in range(n)]
    r = go_to_sp(queue, visited)
    if r:
        queue = r[0]
        ep = r[1]
        visited = [[False] * n for _ in range(n)]
        r2 = go_to_ep(queue, visited, ep)
        queue = r2
        if r2:
            if not start_end:
                print(queue[0][3])
                break
        else:
            print(-1)
            break
    else:
        print(-1)
        break

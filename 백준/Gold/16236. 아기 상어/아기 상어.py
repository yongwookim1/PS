from collections import deque


def bfs(queue: deque, visited: list, n: int, graph: list):
    flag = False
    tq = deque()
    while queue:
        y, x, t, l, eat = queue.popleft()
        for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx]:
                if graph[ny][nx] == 0 or graph[ny][nx] == l:
                    visited[ny][nx] = True
                    queue.append((ny, nx, t + 1, l, eat))
                elif graph[ny][nx] < l:
                    if eat + 1 < l:
                        tq.append((ny, nx, t + 1, l, eat + 1))
                    elif eat + 1 == l:
                        tq.append((ny, nx, t + 1, l + 1, 0))
                    flag = True
    return tq if flag else None


def main():
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

    res = 0
    while True:
        visited = [[False] * n for _ in range(n)]
        visited[queue[0][0]][queue[0][1]] = True
        r = bfs(queue, visited, n, graph)
        if not r:
            print(res)
            break
        else:
            tq = sorted(r, key=lambda x: [x[2], x[0], x[1]])
            queue.append(tq[0])
            graph[queue[0][0]][queue[0][1]] = 0
            res = queue[0][2]


if __name__ == "__main__":
    main()

from collections import deque

n, k = map(int, input().split())

visited = [False] * 100001
visited[n] = True


def bfs():
    queue = deque()
    queue.append((n, 0))
    while queue:
        x, count = queue.popleft()
        if x == k:
            print(count)
            break
        for i in [x * 2, x - 1, x + 1]:
            if 0 <= i < 100001 and visited[i] == False:
                if i == (x * 2):
                    visited[i] = True
                    queue.appendleft((i, count))
                elif i == x - 1 or i == x + 1:
                    visited[i] = True
                    queue.append((i, count + 1))


bfs()

from collections import deque

a, b = map(int, input().split())

queue = deque()
queue.append((a, 1))


def bfs():
    while queue:
        x, count = queue.popleft()
        if x == b:
            return count
        for i in [2 * x, int(str(x) + "1")]:
            if 0 < i <= b:
                queue.append((i, count + 1))
    return -1


print(bfs())

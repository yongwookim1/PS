from collections import deque


def distance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)


def bfs(queue: deque, visited: list):
    while queue:
        x, y = queue.popleft()
        if distance(x, y, end1, end2) <= 1000:
            return "happy"
        for i in range(n):
            cs1, cs2 = cs[i]
            if (cs1, cs2) not in visited and distance(x, y, cs1, cs2) <= 1000:
                visited.append((cs1, cs2))
                queue.append((cs1, cs2))
    return "sad"


for _ in range(int(input())):
    n = int(input())
    start1, start2 = map(int, input().split())
    cs = [tuple(map(int, input().split())) for _ in range(n)]
    end1, end2 = map(int, input().split())
    queue = deque()
    queue.append((start1, start2))
    visited = []
    print(bfs(queue, visited))

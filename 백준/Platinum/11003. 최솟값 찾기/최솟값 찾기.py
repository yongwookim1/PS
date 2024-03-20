from collections import deque

n, l = map(int, input().split())
data = list(map(int, input().split()))
queue = deque()

for i in range(n):
    while queue and data[i] <= queue[-1][0]:
        queue.pop()
    queue.append((data[i], i))
    if queue[0][1] <= i - l:
        queue.popleft()
    print(queue[0][0], end=" ")

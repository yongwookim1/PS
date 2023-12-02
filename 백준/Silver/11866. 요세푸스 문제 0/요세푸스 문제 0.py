from collections import deque

n, k = map(int, input().split())

result = []
queue = deque()

for i in range(1, n + 1):
    queue.append(i)

while queue:
    for i in range(k - 1):
        queue.append(queue.popleft())
    result.append(queue.popleft())

print("<", end="")
for i in range(n - 1):
    print(f"{result[i]}, ", end="")
print(result[-1], end="")
print(">", end="")

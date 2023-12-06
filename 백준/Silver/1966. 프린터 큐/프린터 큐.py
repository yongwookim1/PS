from collections import deque

t = int(input())
for i in range(t):
    queue = deque()
    queue2 = deque()
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    for j in numbers:
        queue.append(j)
    idx = [i for i in range(n)]
    for k in idx:
        queue2.append(k)
    if n == 1:
        print(1)
        continue
    st = 0
    while len(queue) > 1:
        tmp = queue.popleft()
        tmp2 = queue2.popleft()
        if tmp >= max(queue):
            st += 1
            if tmp2 == m:
                print(st)
                break
        else:
            queue.append(tmp)
            queue2.append(tmp2)
    else:
        print(n)

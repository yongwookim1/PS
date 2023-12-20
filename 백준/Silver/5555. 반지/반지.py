from collections import deque

f = input()
n = int(input())
st = 0
for i in range(n):
    word = input()
    queue = deque()
    flag = False
    for j in word:
        queue.append(j)
    queue2 = "".join(queue)
    if f in queue2:
        flag = True
    for k in range(n):
        queue.append(queue.popleft())
        queue2 = "".join(queue)
        if f in queue2:
            flag = True
    if flag == True:
        st += 1
print(st)

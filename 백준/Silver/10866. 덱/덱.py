from collections import deque
import sys

input = sys.stdin.readline

queue = deque()

n = int(input())
for i in range(n):
    order = input().split()
    if order[0] == "push_front":
        queue.appendleft(order[1])
    if order[0] == "push_back":
        queue.append(order[1])
    if order[0] == "pop_front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    if order[0] == "pop_back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())
    if order[0] == "size":
        print(len(queue))
    if order[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    if order[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    if order[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])

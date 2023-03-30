from collections import deque

n = int(input())
list = [0]

for i in range(n):
    list.append(int(input()))

if len(list) == 2:
    print(0)
    exit()

if list[1] == max(list[2:]):
    print(1)
    exit()

ct = 0
while True:
    if list.index(max(list)) == 1 and max(list[2:]) == list[1]:
        ct += 1
        break
    if list.index(max(list)) == 1:
        break
    list[list.index(max(list))] -= 1
    list[1] += 1
    ct += 1

print(ct)
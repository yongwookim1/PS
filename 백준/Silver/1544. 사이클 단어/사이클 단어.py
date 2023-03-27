from collections import deque

n = int(input())
list = []
for i in range(n):
    word = deque(input())
    for j in range(len(word)):
        tmp = ''.join(word)
        if tmp in list:
            break
        word.rotate()
    else:
        list.append(''.join(word))
print(len(list))
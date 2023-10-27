from collections import deque

for i in range(int(input())):
    n = int(input())
    a = list(input().split())
    word = deque()
    for i in a:
        if not word:
            word.append(i)
        else:
            if ord(word[0]) >= ord(i):
                word.appendleft(i)
            else:
                word.append(i)
    print("".join(word))

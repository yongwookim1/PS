from collections import deque

for i in range(int(input())):
    sentence = deque(input().split())
    for j in range(2):
        sentence.append(sentence.popleft())
    print(" ".join(sentence))

from collections import deque

n = int(input())
card = deque([i for i in range(1, n + 1)])
discard = []

while len(card) != 1:
    discard.append(card.popleft())
    card.append(card.popleft())

discard.append(card[0])
print(*discard)

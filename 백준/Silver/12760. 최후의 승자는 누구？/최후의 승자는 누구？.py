n, m = map(int, input().split())

c = [[0] * n for _ in range(m)]
score = [0] * n
for i in range(n):
    cards = list(map(int, input().split()))
    cards.sort(reverse=True)
    for j in range(m):
        c[j][i] = cards[j]

for k in c:
    mx = -1
    ml = []
    for idx, l in enumerate(k):
        if l > mx:
            mx = l
            if ml:
                ml = []
            ml.append(idx)
        elif l == mx:
            ml.append(idx)
    for m in ml:
        score[m] += 1

r = []
for idx, n in enumerate(score, 1):
    if max(score) == n:
        r.append(idx)

print(*r)

from itertools import permutations

p = []

n = int(input())
for i in range(n):
    weight, height = map(int, input().split())
    p.append([weight, height])


result = []
rank = 1
for g, h in enumerate(permutations(p, 2), 1):
    i, j = h
    if i[0] < j[0] and i[1] < j[1]:
        rank += 1
    if g % (n - 1) == 0:
        result.append(rank)
        rank = 1
print(*result)

from itertools import combinations

n = int(input())

names = [input() for _ in range(n)]

st = 0
for i, j in combinations(names, 2):
    leni = len(i)
    lenj = len(j)
    lenij = min(leni, lenj)
    for m in range(lenij):
        if i[-m - 1 :] == j[: m + 1] or j[-m - 1 :] == i[: m + 1]:
            st += 1
            break

print(st)

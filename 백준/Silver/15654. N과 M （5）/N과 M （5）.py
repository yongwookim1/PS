from itertools import permutations

n, m = map(int,input().split())
l = sorted(list(map(int,input().split())))

series = permutations(l, m)

for i in series:
    print(*i)
from itertools import combinations

n, m = map(int,input().split())
l = sorted(list(map(int,input().split())))

series = sorted(list(set(combinations(l, m))))

for i in series:
    print(*i)
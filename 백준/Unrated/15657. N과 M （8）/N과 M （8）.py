from itertools import combinations_with_replacement

n, m = map(int,input().split())
l = sorted(list(map(int,input().split())))

series = combinations_with_replacement(l, m)

for i in series:
    print(*i)
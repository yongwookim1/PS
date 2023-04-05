from itertools import combinations

n, m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()

a = list(combinations(a,m))

for i in a:
    print(*i)
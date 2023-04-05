from itertools import combinations

n, m = map(int,input().split())

series = combinations([i for i in range(1,n+1)], m)

for i in series:
    print(*i)
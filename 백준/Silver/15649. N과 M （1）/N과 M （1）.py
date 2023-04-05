from itertools import combinations, permutations

n, m = map(int,input().split())

series = permutations([i for i in range(1,n+1)], m)

for i in series:
    print(*i)
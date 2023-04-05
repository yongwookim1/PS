from itertools import combinations_with_replacement, permutations

n, m = map(int,input().split())

series = combinations_with_replacement([i for i in range(1,n+1)], m)

for i in series:
    print(*i)
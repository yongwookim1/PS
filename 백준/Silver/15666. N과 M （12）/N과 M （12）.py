from itertools import combinations_with_replacement

n, m = map(int, input().split())

numbers = list(map(int, input().split()))
numbers.sort()

result = []
for a in combinations_with_replacement(numbers, m):
    if a not in result:
        result.append(a)

for i in result:
    print(*i)

from itertools import permutations

n = list(map(int, input()))

n.sort(reverse=True)
if 0 not in n:
    print(-1)
    exit()

if sum(n) % 3 == 0:
    m = "".join(map(str, n))
else:
    m = -1

print(m if m != 0 else -1)

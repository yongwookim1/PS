from itertools import combinations_with_replacement

prime = [True for _ in range(1001)]
prime[0] = prime[1] = False

for i in range(2, int(1001 ** (1 / 2)) + 1):
    if prime[i]:
        for j in range(i * 2, 1001, i):
            prime[j] = False

primes = []
for i in range(1001):
    if prime[i] == True:
        primes.append(i)

for i in range(int(input())):
    n = int(input())
    for j in combinations_with_replacement(primes, 3):
        if sum(j) == n:
            print(*j)
            break
    else:
        print(0)

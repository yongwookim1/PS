import sys

input = sys.stdin.readline

prime = [True for _ in range(1000001)]
prime[0] = prime[1] = False

for i in range(2, int(1000001 ** (1 / 2)) + 1):
    if prime[i]:
        for j in range(i * 2, 1000001, i):
            prime[j] = False

primes = []
for i in range(1000001):
    if prime[i]:
        primes.append(i)

while True:
    n = int(input())
    if n == 0:
        break
    Flag = False
    while Flag == False:
        for i in primes:
            if prime[i] and prime[n - i]:
                print(f"{n} = {i} + {n-i}")
                Flag = True
                break

t = int(input())

prime = [True for _ in range(10001)]

for i in range(2, int(10001 ** (1 / 2)) + 1):
    if prime[i]:
        for j in range(2 * i, 10001, i):
            prime[j] = False

primen = []
for i in range(10001):
    if prime[i]:
        primen.append(i)

for i in range(t):
    n = int(input())
    a = n // 2
    b = n // 2
    while True:
        if prime[a] and prime[b]:
            print(a, b)
            break
        else:
            a -= 1
            b += 1

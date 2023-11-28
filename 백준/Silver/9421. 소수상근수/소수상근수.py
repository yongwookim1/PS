prime = [True for _ in range(1000001)]
prime[0] = prime[1] = False


for i in range(2, int(1000001 ** (1 / 2)) + 1):
    if prime[i] == True:
        for j in range(i * 2, 1000001, i):
            prime[j] = False


n = int(input())
for i in range(3, n + 1):
    if prime[i]:
        sl = []
        s = int(i)
        while True:
            s = sum([int(j) ** 2 for j in str(s)])
            if s == 1:
                print(i)
                break
            if s in sl:
                break
            sl.append(s)

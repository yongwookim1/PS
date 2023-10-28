n, k = map(int, input().split())

st = 0
prime = [True for _ in range(n + 1)]

for i in range(2, n + 1):
    if prime:
        for j in range(i, n + 1, i):
            if prime[j] == True:
                st += 1
            prime[j] = False
            if st == k:
                print(j)
                exit()

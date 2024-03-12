t = int(input())

for _ in range(t):
    n = int(input())
    pigs = list(map(int, input().split()))
    days = 1
    while True:
        s = sum(pigs)
        if s > n:
            print(days)
            break
        npigs = [0] * 6
        for i in range(6):
            npigs[i] = (
                pigs[i] + pigs[(i - 1) % 6] + pigs[(i + 1) % 6] + pigs[(i + 3) % 6]
            )
        pigs = npigs[:]
        days += 1

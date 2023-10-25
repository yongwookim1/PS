t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    na = []
    k = 1
    for i in a:
        for j in range(k, 1000):
            if i != j:
                na.append(j)
                k = j + 1
                break
    print(na[-1])

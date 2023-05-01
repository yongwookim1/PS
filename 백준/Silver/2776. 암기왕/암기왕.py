from collections import defaultdict

t = int(input())
for _ in range(t):
    dd = defaultdict(int)
    n = int(input())
    a = list(map(int,input().split()))
    for i in a:
        dd[i] += 1
    m = int(input())
    b = list(map(int,input().split()))
    for j in b:
        if dd[j] >= 1:
            print(1)
        else:
            print(0)
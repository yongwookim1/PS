n = int(input())

for i in range(n):
    l = list(map(int,input().split()))
    l.remove(i+1)
    nl = []
    st = 0
    for j in l:
        nl.append(j)
        nl.sort()
        for k in nl:
            if k > j:
                st += 1
    print(f'{i+1} {st}')
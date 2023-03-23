n = int(input())
m = 0
ct = 0
l = list(map(int,input().split()))

for i in l:
    if i == m:
        if m == 2:
            m = 0
        else:
            m += 1
        ct += 1

print(ct)
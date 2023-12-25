n = int(input())
p = list(map(int, input().split()))

st = 0
u = []
for i in p:
    if i not in u:
        c = p.count(i)
        if c <= 2:
            st += c
        else:
            st += 2
        u.append(i)

print(st)

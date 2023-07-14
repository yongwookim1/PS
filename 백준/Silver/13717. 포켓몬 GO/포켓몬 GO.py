n = int(input())

me = 0
es = 0
mep = ''
for i in range(n):
    p = input()
    k, m = map(int,input().split())
    e = 0
    while True:
        if m >= k:
            m -= k
            e += 1
            m += 2
        else:
            es += e
            if me < e:
                me = e
                mep = p
            break

print(es)
print(mep)
def p(n,d):
    s = [1] * n
    m = int(n**0.5)
    for i in range(2,m+1):
        if s[i] == 1:
            for j in range(i+i,n,i):
                s[j] = 0
                if d[j] == j:
                    d[j] = i 
a = int(input())
b = list(map(int,input().split()))
g = [i for i in range(5000001)]
c = p(5000001,g)
for i in range(a):
    e = []
    f = b[i]
    while f > 1:
        e.append(g[f])
        f = f // g[f]
    for i in e:
        print(i,end = " ")
    print()
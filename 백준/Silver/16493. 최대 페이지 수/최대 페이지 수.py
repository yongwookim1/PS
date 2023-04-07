from itertools import combinations

n, m = map(int,input().split())

d_list = []
p_list = []
for _ in range(m):
    d,p = map(int,input().split())
    d_list.append(d)
    p_list.append(p)

mx = []
for i in range(1,m+1):
    for j,k in zip(combinations(d_list,i),combinations(p_list,i)):
        s_j = 0
        s_p = 0
        s_j += sum(j)
        s_p += sum(k)
        if s_j <= n:
            mx.append(s_p)

if mx:
    print(max(mx))
else:
    print(0)
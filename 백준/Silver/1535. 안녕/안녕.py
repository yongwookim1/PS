n = int(input())
h = [0] + list(map(int,input().split()))
p = [0] + list(map(int,input().split()))

d = [[0] * 101 for i in range(n+1)]

for i in range(1,n+1):
    for j in range(1,101):
        if j >= h[i]:
            d[i][j] = max(d[i-1][j],d[i-1][j-h[i]]+p[i])
        else:
            d[i][j] = d[i-1][j]

print(d[n][99])
n, m = map(int,input().split())

d = [[0] * m for i in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0 or j ==0:
            d[i][j] = 1
            continue
        try:
            d[i][j] += d[i-1][j-1] % 1000000007
        except:
            pass
        try:
            d[i][j] += d[i][j-1] % 1000000007
        except:
            pass
        try:
            d[i][j] += d[i-1][j] % 1000000007
        except:
            pass

print(d[n-1][m-1] % 1000000007)
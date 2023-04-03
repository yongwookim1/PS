n = int(input())

d = [[0] * 10 for i in range(1001)]
d[1] = [1,1,1,1,1,1,1,1,1,1]

for i in range(2,n+1):
    for j in range(10):
        d[i][j] = sum(d[i-1][j:10])

print(sum(d[n])%10007)
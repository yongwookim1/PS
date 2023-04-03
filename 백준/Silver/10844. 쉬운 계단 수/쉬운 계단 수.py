n = int(input())

d = [[0] * 10 for i in range(101)]
d[1] = [0,1,1,1,1,1,1,1,1,1]
d[2] = [1,1,2,2,2,2,2,2,2,1]

for i in range(3,n+1):
    for j in range(10):
        if j == 0:
            d[i][j] = d[i-1][1]
        elif j == 9:
            d[i][j] = d[i-1][8]
        else:
            d[i][j] = d[i-1][j-1] + d[i-1][j+1]

print(sum(d[n]) % 1000000000)
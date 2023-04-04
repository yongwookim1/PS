n = int(input())

d = [0,1] + [0 for _ in range(n-2)]

for i in range(2,n):
    d[i] = (d[i-1] + d[i-2]) % 1000000007

print(d[n-1])
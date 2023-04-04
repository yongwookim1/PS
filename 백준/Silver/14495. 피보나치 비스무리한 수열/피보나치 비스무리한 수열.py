n = int(input())

d = [0 for _ in range(116)]
d[0], d[1], d[2] = 1, 1, 1

for i in range(3,n):
    d[i] = d[i-1] + d[i-3]

print(d[n-1])
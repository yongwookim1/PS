n = int(input())

d = [0 for _ in range(n+1)]
d[1] = 0
log = []

for i in range(2,n+1):
    d[i] = d[i-1] + 1
    if i % 3 == 0:
        d[i] = min(d[i//3] + 1, d[i])
    if i % 2 == 0:
        d[i] = min(d[i//2] + 1, d[i])

i = n
while i != 1:
    if i % 3 == 0 and d[i//3] == d[i] - 1:
        i //= 3
        log.append(i)
    elif i % 2 == 0 and d[i//2] == d[i] - 1:
        i //= 2
        log.append(i)
    else:
        i -= 1
        log.append(i)

print(d[n])
print(n, *log)
n, k = map(int, input().split())

coin = []
for i in range(n):
    coin.append(int(input()))
coin.sort(reverse=True)

st = 0
for i in coin:
    st += k // i
    k = k % i

print(st)

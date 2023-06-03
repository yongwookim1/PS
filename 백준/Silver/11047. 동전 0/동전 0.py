n, k = map(int, input().split())

coin = []
for i in range(n):
    coin.append(int(input()))

st = 0
for i in coin[::-1]:
    if k >= i:
        while True:
            if k < i:
                break
            k -= i
            st += 1

print(st)

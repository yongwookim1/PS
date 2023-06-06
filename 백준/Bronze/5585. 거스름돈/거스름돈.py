n = int(input())

m = 1000 - n

r = 0
for i in [500, 100, 50, 10, 5, 1]:
    if m >= i:
        r += m // i
        m %= i

print(r)

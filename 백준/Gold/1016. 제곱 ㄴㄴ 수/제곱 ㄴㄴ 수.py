mn, mx = map(int, input().split())

num = [1] * (mx - mn + 1)

for i in range(2, int(mx**0.5) + 1):
    n = i * i
    j = int(mn / n)
    while n * j <= mx:
        if n * j >= mn:
            num[n * j - mn] = 0
            j += 1
        else:
            j += 1

print(sum(num))

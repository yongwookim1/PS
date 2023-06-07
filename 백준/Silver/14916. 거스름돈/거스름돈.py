n = int(input())

q = n // 5
for i in range(q,-1,-1):
    t = n - (i * 5)
    if t % 2 == 0:
        print(i + t // 2)
        break
else:
    print(-1)
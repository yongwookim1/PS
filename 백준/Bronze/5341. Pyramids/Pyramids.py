while True:
    n = int(input())
    if n == 0:
        break
    t = 0
    for i in range(n, 0, -1):
        t += i
    print(t)

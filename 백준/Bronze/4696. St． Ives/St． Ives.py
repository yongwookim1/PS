while True:
    n = float(input())
    if int(n) == 0:
        break
    s = 1
    for i in range(1, 5):
        s += n**i
    print(f"{s:0.2f}")

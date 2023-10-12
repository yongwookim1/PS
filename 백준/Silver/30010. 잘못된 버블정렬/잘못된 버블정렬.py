n = int(input())
if n == 3:
    print(*[3, 1, 2])
    exit()
l = [i for i in range(n, 3, -1)]
l.extend([1, 3, 2])
print(*l)

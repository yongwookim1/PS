def fibo(n):
    if n == 0:
        f = [0]
        return f[n]
    elif n == 1:
        f = [0, 1]
        return f[n]
    else:
        f = [0] * (n + 1)
        f[0] = 0
        f[1] = 1
        for i in range(2, n + 1):
            f[i] = f[i - 1] + f[i - 2]

        return f[n]


n = int(input())
print(fibo(n - 1), fibo(n))

from bisect import bisect_left, bisect_right


def calbi(arr, left, right):
    r = bisect_right(arr, right)
    l = bisect_left(arr, left)
    return r - l


def fibo(n):
    f = [0] * n
    f[0] = 1
    f[1] = 2
    for i in range(2, n):
        f[i] = f[i - 2] + f[i - 1]
    return f


while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    f = fibo(500)
    print(calbi(f, a, b))

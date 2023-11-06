from bisect import bisect_left, bisect_right


def calCountsByRange(nums, left_value, right_value):
    r_i = bisect_right(nums, right_value)
    l_i = bisect_left(nums, left_value)
    return r_i - l_i


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
    f = fibo(1000)
    print(calCountsByRange(f, a, b))

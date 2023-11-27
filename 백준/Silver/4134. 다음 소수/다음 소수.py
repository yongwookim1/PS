def is_prime(n):
    if n == 0:
        return False
    if n == 1:
        return False
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False
    return True


for i in range(int(input())):
    a = int(input())
    while True:
        if is_prime(a):
            print(a)
            break
        else:
            a += 1

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


x, y = map(int, input().split(":"))
z = gcd(x, y)
print(f"{x//z}:{y//z}")

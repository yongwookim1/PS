n = int(input())

def c():
    if a * b >= n:
        print(a, b)
        exit()

a, b = 1, 1
while True:
    c()
    a += 1
    c()
    b += 1
    c()
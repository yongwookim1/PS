for i in range(int(input())):
    n = int(input()) + 1
    while "0" in str(n):
        n += 1
    print(n)

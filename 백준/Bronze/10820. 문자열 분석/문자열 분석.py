while True:
    try:
        a = input()
        l, u , d, b = 0, 0, 0, 0
        for i in a:
            if i.islower():
                l += 1
            elif i.isupper():
                u += 1
            elif i.isdigit():
                d += 1
            else:
                b += 1
        print(l, u, d, b)
    except EOFError:
        break
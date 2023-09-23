for i in range(int(input())):
    inp = input()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s = 0
    for j in inp:
        if j in alpha:
            alpha = alpha.replace(j, "")

    for k in alpha:
        s += ord(k)

    print(s)

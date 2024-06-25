while True:
    nl = list(map(int, input().split()))
    if nl[0] == -1:
        break
    st = 0
    for i in nl:
        if i != 0 and i * 2 in nl:
            st += 1
    print(st)

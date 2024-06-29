N = int(input())

for i in range(N):
    g = int(input())
    sns = []
    for j in range(g):
        sn = int(input())
        sns.append(sn)
    start = 1
    flag = False
    while flag == False:
        rest = []
        for k in sns:
            if k % start in rest:
                start += 1
                break
            else:
                rest.append(k % start)
        else:
            flag = True
    print(start)

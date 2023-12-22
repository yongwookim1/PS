while True:
    try:
        a, b = map(int, input().split())

        st = 0
        for number in range(a, b + 1):
            p = []
            for i in str(number):
                if i not in p:
                    p.append(i)
                else:
                    break
            else:
                st += 1

        print(st)
    except:
        break

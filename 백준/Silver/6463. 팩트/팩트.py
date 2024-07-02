while True:
    try:
        n = int(input())
        r = 1
        for i in range(2, n + 1):
            r *= i
            while True:
                if str(r)[-1] == "0":
                    r //= 10
                else:
                    break
            r = int(str(r)[-100:])
        print(f"{n:>5} -> {str(r)[-1]}")
    except:
        break

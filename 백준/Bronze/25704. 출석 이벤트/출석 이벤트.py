n = int(input())
p = int(input())

if n >= 20:
    if p * 75/100 <= p - 2000:
        print(int(p * 75/100))
    else:
        if p - 2000 >= 0:
            print(p - 2000)
        else:
            print(0)
elif n >= 15:
    if p * 90/100 <= p - 2000:
        print(int(p * 90/100))
    else:
        if p - 2000 >= 0:
            print(p - 2000)
        else:
            print(0)
elif n >= 10:
    if p * 90/100 <= p - 500:
        print(int(p * 90/100))
    else:
        if p - 500 >= 0:
            print(p - 500)
        else:
            print(0)
elif n >= 5:
    if p - 500 >= 0:
        print(p - 500)
    else:
        print(0)
else:
    print(p)
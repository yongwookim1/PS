n = int(input())

x = [64]
while True:
    if sum(x) > n:
        smallest = x[-1]
        if smallest//2+sum(x[:-1]) >= n:
            x.pop()
            x.append(smallest//2)
        else:
            x.pop()
            x.append(smallest//2)
            x.append(smallest//2)
        if sum(x) == n:
            print(len(x))
            break
    else:
        print(len(x))
        break
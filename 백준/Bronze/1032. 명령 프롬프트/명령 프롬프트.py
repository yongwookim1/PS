for i in range(int(input())):
    if i == 0:
        a = list(input())
    else:
        b = list(input())
        for j in range(len(a)):
            if a[j] != b[j]:
                a[j] = '?'
print(''.join(a))
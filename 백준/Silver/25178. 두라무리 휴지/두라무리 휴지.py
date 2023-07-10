n = int(input())
a = input()
b = input()

if sorted(a) == sorted(b) and a[0] == b[0] and a[-1] == b[-1]:
    for i in a:
        if i in ['a','e','i','o','u']:
            a = a.replace(i,'')
    for j in b:
        if j in ['a','e','i','o','u']:
            b = b.replace(j,'')
    if a==b:
        print("YES")
        exit()
    else:
        print("NO")
        exit()
else:
    print("NO")
        
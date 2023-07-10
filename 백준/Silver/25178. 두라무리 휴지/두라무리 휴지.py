n = int(input())
a = input()
b = input()

if sorted(a) == sorted(b) and a[0] == b[0] and a[-1] == b[-1]:
    for i in 'aeiou':
        a = a.replace(i,'')
        b = b.replace(i,'')
    if a==b:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
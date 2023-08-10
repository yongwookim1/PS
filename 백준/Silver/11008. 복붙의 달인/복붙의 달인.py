n = int(input())
for i in range(n):
    s, p = input().split()
    s = s.replace(p, '0')
    print(len(s))
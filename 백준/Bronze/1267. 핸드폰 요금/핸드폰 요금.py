n = int(input())
a = list(map(int,input().split()))

y = 0 
m = 0
for i in a:
    y += (i // 30 + 1) * 10
    m += (i // 60 + 1) * 15

if y > m:
    print(f"M {m}")
elif y < m:
    print(f"Y {y}")
else:
    print(f"Y M {y}")
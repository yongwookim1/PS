n = int(input())
l = [int(input()) for i in range(n)]

st = 1
m = l[-1]
for i in l[:-1][::-1]:
    if i > m:
        m = i
        st += 1

print(st)

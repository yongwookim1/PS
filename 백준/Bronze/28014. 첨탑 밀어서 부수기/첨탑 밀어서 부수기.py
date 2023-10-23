n = int(input())
a = list(map(int, input().split()))
m = 0
st = 0
for i in a:
    if i >= m:
        st += 1
        m = i
    else:
        m = i
print(st)

n,k,l=map(int,input().split())
st = 0
li = []
for i in range(n):
    a, b ,c = map(int,input().split())
    if a + b + c >= k and a >= l and b >= l and c >= l:
        st += 1
        li.extend([a,b,c])
print(st)
print(*li)
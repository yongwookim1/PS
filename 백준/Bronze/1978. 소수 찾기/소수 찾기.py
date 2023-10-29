def prime(n):
    st = 0
    if n == 1: return False
    if n == 2: return True
    for i in range(2,n):
        if n % i == 0:
            st += 1
    if st > 0: return False
    else: return True

n = int(input())
a = list(map(int,input().split()))
st = 0
for j in a:
    if prime(j) == True:
        st += 1
print(st)
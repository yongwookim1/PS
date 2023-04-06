def prime(n):
    if n == 1: return False
    if n == 2: return True
    st = 0
    for i in range(2,n):
        if n % i == 0:
            st += 1
            if st > 0:
                return False
    if st == 0: return True
def p(n):
    if str(n) == str(n)[::-1]: return True
    else: return False

n = int(input())
br = False
for i in range(n,n+1000000):
    if p(i) == True and prime(i) == True:
        print(i)
        br = True
    if br == True: break
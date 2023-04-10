import math

def isprime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def np(n):
    if len(str(n)) == a:
        print(n)
    else:
        for i in [1,3,5,7,9]:
            nn = 10 * n + i
            if isprime(nn) == True:
                np(nn)

a = int(input())
for i in [2,3,5,7]:
    np(i)
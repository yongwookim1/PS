import math
import sys
input = sys.stdin.readline

a, b = map(int,input().split())
if b > 10000000:
    b = 10000000
    
array = [True for _ in range(b+1)]

for i in range(2,int(math.sqrt(b)+1)):
    if array[i] == True:
        j = 2
        while i*j <= b:
            array[i*j] = False
            j += 1

for j in range(a,b+1):
    if array[j] == True and str(j) == str(j)[::-1]:
        print(j)
print(-1)
a, b = map(int,input().split())
s = 1

for i in range(a,b+1):
    s *= sum([i for i in range(1,i+1)])

print(s%14579)
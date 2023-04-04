import sys
input = sys.stdin.readline

n, m = map(int,input().split())

dict = {}
dict2 = {}
for i in range(1,n+1):
    mon = input().rstrip()
    dict[i] = mon
    dict2[mon] = i

for _ in range(m):
    a = input().rstrip()
    if a.isdigit():
        print(dict[int(a)])
    else:
        print(dict2[a])
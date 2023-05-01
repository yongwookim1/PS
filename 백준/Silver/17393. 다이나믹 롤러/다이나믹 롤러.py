from bisect import bisect_right

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
for i, j in enumerate(a, 1):
    print(bisect_right(b,j) - i)
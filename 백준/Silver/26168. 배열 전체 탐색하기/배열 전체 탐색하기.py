from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
lenA = len(A)
for _ in range(m):
    B = list(map(int,input().split()))
    a = B[0]
    if a == 1:
        b = B[1]
        print(lenA - bisect_left(A,b))
    elif a == 2:
        b = B[1]
        print(lenA - bisect_right(A,b))
    else:
        b, c = B[1], B[2]
        print(bisect_right(A,c) - bisect_left(A,b))
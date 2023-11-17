import sys
import math

input = sys.stdin.readline

t = int(input())
for i in range(t):
    M, N, x, y = map(int, input().split())

    for i in range(x, M * N // math.gcd(M, N) + 1, M):
        if i % M == 0:
            p = M
        else:
            p = i % M
        if i % N == 0:
            q = N
        else:
            q = i % N
        if p == x and q == y:
            print(i)

            break
    else:
        print(-1)

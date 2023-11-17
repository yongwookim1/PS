import sys
import math

input = sys.stdin.readline

t = int(input())
for i in range(t):
    M, N, x, y = map(int, input().split())

    for i in range(x, M * N // math.gcd(M, N) + 1, M):
        if (i - y) % N == 0:
            print(i)
            break
    else:
        print(-1)

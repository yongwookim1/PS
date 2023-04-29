import sys
from collections import defaultdict
input = sys.stdin.readline

while True:
    sang_list = defaultdict(bool)
    n, m = map(int,input().split())
    if n == 0 and m == 0:
        break
    st = 0
    for _ in range(n):
        sang_list[int(input())] = True
    for _ in range(m):
        if sang_list[int(input())]:
            st += 1

    print(st)
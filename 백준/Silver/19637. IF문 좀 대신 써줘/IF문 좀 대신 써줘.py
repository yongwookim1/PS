import sys
from bisect import bisect_left
input = sys.stdin.readline

n, m = map(int,input().split())
title_list = []
score_list = []
for _ in range(n):
    title, score = input().split()
    score = int(score)
    title_list.append(title)
    score_list.append(score)

for i in range(m):
    input_power = int(input())
    print(title_list[bisect_left(score_list, input_power)])
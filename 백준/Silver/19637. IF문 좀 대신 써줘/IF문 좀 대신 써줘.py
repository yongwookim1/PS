import sys
input = sys.stdin.readline

def bs(arr: list, x) -> int:
    start = 0
    end = len(arr) - 1
    while start < end:
        mid = (start+end) // 2
        if arr[mid] < x:
            start = mid + 1
        else:
            end = mid
    return start

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
    print(title_list[bs(score_list, input_power)])
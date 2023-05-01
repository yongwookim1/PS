from bisect import bisect_left
import sys
input = sys.stdin.readline


def binary_search(array, start, end, target):
    start = 0
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return bisect_left(array, target)
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1


n, m = map(int,input().split())
a = [int(input()) for _ in range(n)]
a.sort()
for i in range(m):
    target = int(input())
    print(binary_search(a, 0, n-1, target))
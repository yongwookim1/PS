from bisect import bisect_left, bisect_right

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a.sort()


def search(arr, target):
    left = bisect_left(arr, target)
    right = bisect_right(arr, target)
    return right - left


r = []
for i in b:
    r.append(search(a, i))

print(*r)

import copy
from bisect import bisect_left

m, n = map(int,input().split())

a = list(map(int,input().split()))
if sum(a) < m:
    print(0)
    exit()

start = 1
end = max(a)
while start <= end:
    mid = (start+end) // 2
    st = 0
    for snack in a:
        if snack >= mid:
            st += snack // mid
    if st >= m:
        res = mid
        start = mid + 1
    else:
        end = mid - 1

print(res)
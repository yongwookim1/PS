n, m = map(int,input().split())
l = list(map(int,input().split()))

start = 0
end = max(l)


while start <= end:
    mid = (start+end) // 2
    total = 0
    for tree in l:
        if tree > mid:
            total += (tree - mid)
    if total < m:
        end = mid - 1
    else:
        res = mid
        start = mid + 1

print(res)
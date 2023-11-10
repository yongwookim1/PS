n, m = map(int, input().split())

trees = list(map(int, input().split()))

start = 0
end = max(trees)
while start <= end:
    mid = (start + end) // 2

    s = 0
    for i in trees:
        if i > mid:
            s += i - mid

    if s >= m:
        res = mid
        start = mid + 1
    else:
        end = mid - 1

print(res)

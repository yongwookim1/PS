n = int(input())
a = list(map(int,input().split()))
m = int(input())
a.sort()

start = 0
end = max(a)

result = 0
while start <= end:
    mid = (start + end) // 2
    total = sum([mid if x >= mid else x for x in a])
    if total > m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
if result == 0:
    print(max(a))
else:
    print(result)
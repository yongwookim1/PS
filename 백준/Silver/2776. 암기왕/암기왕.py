def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return 1
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return 0


t = int(input())

for i in range(t):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    m = int(input())
    b = list(map(int, input().split()))

    for i in b:
        print(binary_search(a, i))

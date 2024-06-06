n = int(input())

lt = list(map(int, input().split()))

for i in range(len(lt)):
    lt[i] = lt[i] - (n - i)

print(max(lt))

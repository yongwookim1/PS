n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

r = 0
for i, j in zip(a, b):
    r += abs(i - j)

print(r // 2)

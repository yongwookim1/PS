import time

a, b, c, m = map(int, input().split())

fatigue = 0
work = 0

for i in range(24):
    if fatigue + a <= m:
        work += b
        fatigue += a
    else:
        fatigue = max(0, fatigue - c)

print(work)

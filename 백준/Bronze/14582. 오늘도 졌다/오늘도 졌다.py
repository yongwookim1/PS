t1 = list(map(int, input().split()))
t2 = list(map(int, input().split()))

t1_score = 0
t2_score = 0
flag = 0
for i, j in zip(t1, t2):
    t1_score += i
    if t1_score > t2_score:
        flag = True
    t2_score += j

print("Yes" if t2_score > t1_score and flag else "No")

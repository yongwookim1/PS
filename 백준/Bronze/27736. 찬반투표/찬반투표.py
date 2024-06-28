n = int(input())

vote = list(map(int, input().split()))

mj = n // 2
if n % 2 == 1:
    mj += 1

yes = 0
no = 0
wd = 0
for i in vote:
    if i == 1:
        yes += 1
    elif i == -1:
        no += 1
    elif i == 0:
        wd += 1

if wd >= mj:
    print("INVALID")
elif yes <= no:
    print("REJECTED")
else:
    print("APPROVED")

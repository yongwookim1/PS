l = list(map(int, input().split()))

for i in range(1, 10000000000 + 1):
    st = 0
    for j in l:
        if i % j == 0:
            st += 1
    if st >= 3:
        print(i)
        break

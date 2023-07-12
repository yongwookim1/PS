t = int(input())
a = list(map(int,input().split()))

for i in a:
    st = 0
    for j in range(1,i):
        if i % j == 0:
            st += j
    if st < i:
        print("Deficient")
    elif st == i:
        print("Perfect")
    else:
        print("Abundant")
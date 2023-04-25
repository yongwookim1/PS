n = int(input())
q = [int(input()) for _ in range(n)]

for i in q:
    if bin(i)[2] == '1' and '1' not in bin(i)[3:]:
        print(1)
    else:
        print(0)
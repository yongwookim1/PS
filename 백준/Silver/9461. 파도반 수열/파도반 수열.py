list = [int(input()) for i in range(int(input()))]
for i in range(len(list)):
    p = [0 for _ in range(101)]
    p[0], p[1], p[2], p[3], p[4] = 1, 1, 1, 2, 2
    for j in range(5, list[i]):
        p[j] = p[j-2] + p[j-3]
    print(p[list[i]-1])
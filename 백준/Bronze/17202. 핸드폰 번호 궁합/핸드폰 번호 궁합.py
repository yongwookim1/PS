a = list(map(int, input()))
b = list(map(int, input()))

alpha = [[] * i for i in range(14)]

c = []
for i, j in zip(a, b):
    c.append(i)
    c.append(j)

for j in range(len(c) - 1):
    tmp = (c[j] + c[j + 1]) % 10
    alpha[0].append(tmp)

for i in range(1, 14):
    for j in range(len(alpha[i - 1]) - 1):
        tmp = (alpha[i - 1][j] + alpha[i - 1][j + 1]) % 10
        alpha[i].append(tmp)

r = int("".join(map(str, alpha[-1])))
print(f"{r:02d}")

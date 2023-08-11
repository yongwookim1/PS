n = int(input())
foods = list(input())

j = 0
for food in foods:
    if food != 'C':
        j += 1

if j == 0:
    print(n)
    exit()

c = n - j
if c % (j+1) == 0:
    print(c // (j+1))
else:
    print(c // (j+1) + 1)

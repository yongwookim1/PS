dad = list(input().split())
mom = list(input().split())

parents = dad + mom

baby = []
for i in parents:
    for j in parents:
        if [i, j] not in baby:
            baby.append([i, j])

baby.sort(key=lambda x: [x[0], x[1]])

for i, j in baby:
    print(i, j)

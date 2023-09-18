n = int(input())
names = list(input().split())
names_dict = []
for i in names:
    names_dict.append([i, 0])
for i in range(n):
    love = list(input().split())
    for j in love:
        for i in names_dict:
            if i[0] == j:
                i[1] += 1

names_dict.sort(key=lambda x: [-x[1], x[0]])

for i in names_dict:
    print(*i)

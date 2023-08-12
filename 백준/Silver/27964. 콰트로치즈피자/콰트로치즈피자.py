n = input()

c = list(input().split())
nc = []
for i in c:
    if len(i) < 6:
        pass
    elif i[-6:] == 'Cheese':
        nc.append(i)

nc = list(set(nc))
print('yummy' if len(nc) >= 4 else 'sad')
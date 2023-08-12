n = input()

c = {i for i in input().split()}

ct = 0
for i in c:
    if i.endswith('Cheese'):
        ct += 1

print('yummy' if ct >= 4 else 'sad')
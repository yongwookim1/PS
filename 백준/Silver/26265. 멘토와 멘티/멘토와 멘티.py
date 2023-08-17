n = int(input())

l = []
for i in range(n):
    l.append(input().split())

l.sort(key=lambda x: x[1], reverse=True)
l.sort(key=lambda x: x[0])

for j in l:
    print(*j)
    
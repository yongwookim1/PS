n = int(input())

l = []
for i in range(n):
    b, p, q, r = map(int,input().split())
    point1 = p * q * r
    point2 = p + q + r
    l.append([b, point1, point2])

l = sorted(l, key = lambda x : [x[1], x[2], x[0]])

print(*[i[0] for i in l[:3]])
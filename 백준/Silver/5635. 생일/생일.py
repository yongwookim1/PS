n = int(input())

infos = []

for i in range(n):
    info = list(input().split())
    infos.append(info)
    
infos.sort(key = lambda x: [int(x[3]), int(x[2]), int(x[1])])

print(infos[-1][0])
print(infos[0][0])
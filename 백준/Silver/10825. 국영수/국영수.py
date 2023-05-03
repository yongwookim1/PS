import sys
input = sys.stdin.readline

l = []
for i in range(int(input())):
    name, k, e, m = input().split()
    k, e, m = int(k), int(e), int(m)
    l.append([name, k, e, m])

l.sort(key=lambda x: [-x[1],x[2],-x[3],x[0]])

for i in range(len(l)):
    print(l[i][0])
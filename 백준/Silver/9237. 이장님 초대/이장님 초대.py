n = int(input())

a = list(map(int,input().split()))
a.sort(reverse=True)

day = 1
r = []
for i in a:
    r.append(1+i+day)
    day += 1

print(max(r))
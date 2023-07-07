n, l = map(int,input().split())

i = 1
li = []
while True:
    if len(li) == n:
        break
    if str(l) not in str(i):
        li.append(i) 
    i += 1

print(li[-1])
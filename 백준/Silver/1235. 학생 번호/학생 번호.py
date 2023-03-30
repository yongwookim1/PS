from itertools import combinations

n = int(input())

list = []
for i in range(n):
    w = input()
    list.append(w)

list2 = []
ct = 0
st = 0
for j in range(len(w)):
    ct += 1
    list2 = [k[-(j+1):] for k in list]
    for l, m in combinations(list2, 2):
        if l == m:
            st += 1
    if st == 0:
        break
    list2 = []
    st = 0
print(ct)
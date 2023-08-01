n = int(input())

st = 0
camp = [0] * 200001
for _ in range(n):
    number, note = map(int,input().split())
    if note == 1:
        if camp[number] == 0:
            camp[number] = 1
        else:
            st += 1
    elif note == 0:
        if camp[number] == 1:
            camp[number] = 0
        else:
            st += 1

for i in camp:
    if i == 1:
        st += 1

print(st)

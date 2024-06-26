n = int(input())

pws = []
for _ in range(n):
    pw = input()
    pws.append(pw)

for pw in pws:
    if pw[::-1] in pws:
        print(len(pw), pw[len(pw) // 2])
        break

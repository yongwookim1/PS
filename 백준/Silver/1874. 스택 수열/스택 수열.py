n = int(input())
stack = []
pm = []
nb = 1
for i in range(1, n + 1):
    number = int(input())
    if number not in stack:
        for j in range(nb, number + 1):
            stack.append(j)
            pm.append("+")
        nb = stack.pop()
        nb += 1
        pm.append("-")
    else:
        while True:
            if stack[-1] != number:
                print("NO")
                exit()
            p = stack.pop()
            pm.append("-")
            if p == number:
                break
for j in pm:
    print(j)

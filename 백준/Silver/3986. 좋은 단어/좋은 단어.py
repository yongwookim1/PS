st = 0
for i in range(int(input())):
    l = input()
    stack = []
    for i in l:
        if not stack:
            stack.append(i)
        else:
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
    if not stack:
        st += 1
print(st)
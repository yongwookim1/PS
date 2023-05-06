l = input()
llen = len(l)
stack = []
for i in l:
    if i == '(':
        stack.append(i)
    else:
        if not stack:
            stack.append(i)
        elif stack:
            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
print(len(stack))
while True:
    s = input()
    if s == '.':
        break
    stack = []
    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if not stack:
                print('no')
                break
            elif stack and stack[-1] == '(':
                stack.pop()
            else:
                print('no')
                break
        elif i == ']':
            if not stack:
                print('no')
                break
            elif stack and stack[-1] == '[':
                stack.pop()
            else:
                print('no')
                break
    else:
        if stack:
            print('no')
        else:
            print('yes')
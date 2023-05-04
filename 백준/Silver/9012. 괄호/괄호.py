import sys
input = sys.stdin.readline

for i in range(int(input())):
    l = input().rstrip()
    stack = []
    for i in l:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                print("NO")
                break
            else:
                if stack.pop() == '(':
                    pass
    else:
        if not stack:
            print("YES")
        else:
            print("NO")
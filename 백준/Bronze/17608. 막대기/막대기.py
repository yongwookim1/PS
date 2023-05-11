import sys
input = sys.stdin.readline

n = int(input())
l = [int(input()) for i in range(n)]
stack = []

st = 0
for i in l[::-1]:
    if not stack:
        stack.append(i)
        st += 1
    else:
        if stack[-1] < i:
            stack.append(i)
            st += 1

print(st)

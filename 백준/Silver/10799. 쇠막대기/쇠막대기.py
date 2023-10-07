a = list(input())

stack = []
st = 0
stick = 0
for i in a:
    if i == "(":
        stack.append("(")
        stick += 1
        pb = "("
    elif i == ")":
        if pb == "(":
            stack.pop()
            if stick != 0:
                stick -= 1
            st += stick
            pb = ")"
        elif pb == ")":
            stick -= 1
            st += 1
            pb = ")"

print(st)

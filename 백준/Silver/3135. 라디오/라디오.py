a, b = map(int, input().split())

start = []
start.append(a)
n = int(input())
for i in range(n):
    button = int(input())
    if button < b:
        start.append(button - 1)
    else:
        start.append(button + 1)

distances = [abs(i - b) for i in start]

print(min(distances))

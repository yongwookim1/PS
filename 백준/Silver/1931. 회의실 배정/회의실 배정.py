n = int(input())

meeting = []
for i in range(n):
    s, e = map(int, input().split())
    meeting.append([s, e])

meeting.sort(key=lambda x: [x[1], x[0]])

st = 0
tmpend = 0
for start, end in meeting:
    if tmpend <= start:
        st += 1
        tmpend = end

print(st)

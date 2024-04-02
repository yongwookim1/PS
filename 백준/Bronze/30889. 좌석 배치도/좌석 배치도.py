graph = [["."] * 20 for _ in range(10)]

n = int(input())
for _ in range(n):
    seat = input()
    ap = seat[0]
    num = int(seat[1:]) - 1
    apn = ord(ap) - 65
    graph[apn][num] = "o"

for i in graph:
    print(*i, sep="")

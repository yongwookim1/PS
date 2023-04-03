n = int(input())

graph = [list(map(int,input().split())) for _ in range(n)]
if n == 1:
    print(graph[0][0])
    exit()

d = [[0] * i for i in range(1,n+1)]
d[0][0] = graph[0][0]
d[1][0] = graph[0][0] + graph[1][0]
d[1][1] = graph[0][0] + graph[1][1]

for i in range(2,n):
    for j in range(i+1):
        if j == 0:
            d[i][j] = graph[i][j] + d[i-1][j]
            continue
        if j == i:
            d[i][j] = graph[i][j]  + d[i-1][j-1]
            continue
        d[i][j] += max(graph[i][j] + d[i-1][j-1], graph[i][j] + d[i-1][j])

print(max(d[n-1]))
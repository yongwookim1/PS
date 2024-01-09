import sys

n, m, b = map(int, input().split())

answer = sys.maxsize
idx = 0

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

result = []
for height in range(257):
    exceed = 0
    lack = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] >= height:
                exceed += graph[i][j] - height
            else:
                lack += height - graph[i][j]
    if exceed + b >= lack:
        if exceed * 2 + lack <= answer:
            answer = exceed * 2 + lack
            idx = height

print(answer, idx)

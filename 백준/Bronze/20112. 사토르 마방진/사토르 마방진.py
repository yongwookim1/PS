n = int(input())

graph = []
for i in range(n):
    graph.append(list(input()))

ngraph = []
for i in range(n):
    for j in range(n):
        ngraph.append(graph[j][i])

nngraph = []
for i in range(0, n):
    nngraph.append(ngraph[i * n : (i + 1) * n])

if graph == nngraph:
    print("YES")
else:
    print("NO")

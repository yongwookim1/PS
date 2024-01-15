import sys

input = sys.stdin.readline

n = int(input().rstrip())

graph = list(map(int, input().rstrip().split()))
mx = graph
mn = graph

for i in range(1, n):
    graph = list(map(int, input().rstrip().split()))
    mx = [
        graph[0] + max(mx[0], mx[1]),
        graph[1] + max(mx),
        graph[2] + max(mx[1], mx[2]),
    ]
    mn = [
        graph[0] + min(mn[0], mn[1]),
        graph[1] + min(mn),
        graph[2] + min(mn[1], mn[2]),
    ]

print(max(mx), min(mn))

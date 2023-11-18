import sys
sys.setrecursionlimit(10**5)

while True:
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        break
    graph = []
    for i in range(h):
        graph.append(list(map(int,input().split())))

    def dfs(x,y):
        if x <= -1 or x >= w or y <= -1 or y >= h:
            return False
        elif graph[y][x] == 1:
            graph[y][x] = 0
            dfs(x-1,y)
            dfs(x+1,y)
            dfs(x,y-1)
            dfs(x,y+1)
            dfs(x-1,y-1)
            dfs(x+1,y-1)
            dfs(x-1,y+1)
            dfs(x+1,y+1)
            return True
        return False

    ct = 0
    for i in range(w):
        for j in range(h):
            if dfs(i,j) == True:
                ct += 1
    print(ct)
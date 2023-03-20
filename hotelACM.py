N = int(input())

for i in range(N):
    h, w, n = map(int,input().split())
    y = ((n-1) % h) + 1
    x = ((n-1) // h) + 1
    print(f"{y}{x:02d}")
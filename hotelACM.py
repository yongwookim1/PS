N = int(input())

for i in range(N):
    h, w, n = map(int,input().split())
    y = n % h
    x = (n // h) + 1
    print(f"{y}{x:02d}")
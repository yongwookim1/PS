for i in range(int(input())):
    blank = input()
    N = int(input())
    s = 0
    for _ in range(N):
        s += int(input())
    print("YES" if s % N == 0 else "NO")
i = 0
while True:
    i += 1
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break
    print(f"Case {i}: {(V // P) * L + (min(L, V % P))}")

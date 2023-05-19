for i in range(int(input())):
    sentence = list(input().split())
    ns = []
    for j in sentence:
        ns.append(j[::-1])
    print(" ".join(ns))

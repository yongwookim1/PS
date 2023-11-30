m, n = map(int, input().split())

graph = []
for i in range(m):
    graph.append(list(input()))

wl = []
st = 0
for i in range(m - 8 + 1):
    for j in range(n - 8 + 1):
        w = 0
        b = 0
        st += 1
        for k, l in enumerate([row[j : j + 8] for row in graph[i : i + 8]]):
            # 1 == "W"
            if k % 2 == 0:
                for p, q in enumerate(l):
                    if p % 2 == 0:
                        if q == "B":
                            w += 1
                    else:
                        if q == "W":
                            w += 1
            if k % 2 == 1:
                for p, q in enumerate(l):
                    if p % 2 == 0:
                        if q == "W":
                            w += 1
                    else:
                        if q == "B":
                            w += 1
            # 1 == "B"
            if k % 2 == 0:
                for p, q in enumerate(l):
                    if p % 2 == 0:
                        if q == "W":
                            b += 1
                    else:
                        if q == "B":
                            b += 1
            if k % 2 == 1:
                for p, q in enumerate(l):
                    if p % 2 == 0:
                        if q == "B":
                            b += 1
                    else:
                        if q == "W":
                            b += 1

        wl.append(min([w, b]))
print(min(wl))

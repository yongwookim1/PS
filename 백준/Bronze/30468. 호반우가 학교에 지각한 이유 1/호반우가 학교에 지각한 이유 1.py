s, d, i, l, n = map(int, input().split())

need = 4 * n - (s + d + i + l)

print(need if need > 0 else 0)

w, h, b = map(int, input().split())

result = (w - (2 * b)) * (h - (2 * b))

print(0 if (w - (2 * b)) <= 0 or (h - (2 * b)) <= 0 else result)

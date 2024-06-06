d1, d2, d3 = map(int, input().split())

b_c = d1 - d2
b = (b_c + d3) / 2
a = d1 - b
c = d3 - b
if (
    int(a + b) == d1
    and int(a + c) == d2
    and int(b + c) == d3
    and a > 0
    and b > 0
    and c > 0
):
    print(1)
    print(round(a, 1), round(b, 1), round(c, 1))
else:
    print(-1)

s = 0
sh = 0
for i in range(20):
    subject, h, score = input().split()
    h = float(h)
    if score == "A+":
        s += h * 4.5
    if score == "A0":
        s += h * 4.0
    if score == "B+":
        s += h * 3.5
    if score == "B0":
        s += h * 3.0
    if score == "C+":
        s += h * 2.5
    if score == "C0":
        s += h * 2.0
    if score == "D+":
        s += h * 1.5
    if score == "D0":
        s += h * 1.0
    if score == "F":
        s += h * 0
    if score != "P":
        sh += h
print(s / sh)

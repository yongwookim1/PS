n = int(input())

b = 3
fb = (b - 2) ** 2
while n > fb:
    b += 1
    fb = (b - 2) ** 2

print("x" * b)
for i in range(b - 2):
    print("x", "." * (b - 2), "x", sep="")
print("x" * b)

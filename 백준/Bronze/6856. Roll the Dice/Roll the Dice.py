n1 = int(input())
n2 = int(input())

st = 0
for i in range(1, n1 + 1):
    for j in range(1, n2 + 1):
        if i + j == 10:
            st += 1
            break

print(
    f"There are {st} ways to get the sum 10."
    if st != 1
    else f"There is {st} way to get the sum 10."
)

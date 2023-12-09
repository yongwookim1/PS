n = int(input())
word = input()

hash = 0
for i, j in enumerate(word):
    hash += (ord(j) - 96) * (31**i)

hash %= 1234567891
print(hash)

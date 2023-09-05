word = input()

vowels = ["a", "e", "i", "o", "u"]
if word[0] in vowels:
    for i, j in enumerate(word[1:]):
        if i % 2 == 0:
            if j in vowels:
                print(0)
                exit()
        elif i % 2 == 1:
            if j not in vowels:
                print(0)
                exit()
else:
    for i, j in enumerate(word[1:]):
        if i % 2 == 0:
            if j not in vowels:
                print(0)
                exit()
        elif i % 2 == 1:
            if j in vowels:
                print(0)
                exit()
print(1)

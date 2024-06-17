for _ in range(int(input())):
    word = input()
    check_letter = ""
    new_letter = ""
    for letter in word:
        if check_letter != letter:
            new_letter += letter
            check_letter = letter
    print(new_letter)

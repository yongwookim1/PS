for i in range(int(input())):
    prob = input()
    if prob == "P=NP":
        print("skipped")
    else:
        a, b = map(int, prob.split("+"))
        print(a + b)

company = []
for _ in range(int(input())):
    name, record = input().split()
    if record == "enter":
        company.append(name)
    else:
        company.remove(name)

company.sort(reverse=True)
for i in company:
    print(i)

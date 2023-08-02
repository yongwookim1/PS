n = int(input())
for i in range(n):
    city_list = []
    t = int(input())
    for i in range(t):
        city_list.append(input())
    city_list = set(city_list)
    print(len(city_list))
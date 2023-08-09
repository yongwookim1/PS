b, c, d = map(int,input().split())

burger = sorted(list(map(int,input().split())),reverse=True)
side = sorted(list(map(int,input().split())),reverse=True)
beverage = sorted(list(map(int,input().split())), reverse=True)

print(sum(burger) + sum(side) + sum(beverage))

l = min(b, c, d)

sale = int(sum(burger[:l] + side[:l] + beverage[:l]) * (9/10))
add = sum(burger[l:] + side[l:] + beverage[l:])
print(sale + add)

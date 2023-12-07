from collections import defaultdict

n = int(input())

numbers = []
for i in range(n):
    a = int(input())
    numbers.append(a)

print(round(sum(numbers) / n))
print(sorted(numbers)[n // 2])
dic = defaultdict(int)
for i in numbers:
    dic[i] += 1
num_items = defaultdict(list)
for k, v in dic.items():
    num_items[v].append(k)
if len(num_items[max(num_items.keys())]) > 1:
    print(sorted(num_items[max(num_items.keys())])[1])
else:
    print(sorted(num_items[max(num_items.keys())])[0])
print(max(numbers) - min(numbers))

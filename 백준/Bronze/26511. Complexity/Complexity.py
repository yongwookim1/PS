from collections import defaultdict

for i in range(int(input())):
    word = input()
    counter = defaultdict(int)
    for j in word:
        counter[j] += 1
    v = sorted(list(counter.values()))
    print(sum(counter.values()) - sum(v[-2:]))

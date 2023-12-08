n = int(input())
if n == 0:
    print(0)
    exit()


def my_round(n):
    if n % 0.5 == 0 and n % 1 != 0:
        n = int(n) + 1
    else:
        n = round(n)
    return n


cut = my_round(n * 0.15)
scores = []
for i in range(n):
    score = int(input())
    scores.append(score)

my_scores = sorted(scores)[cut : n - cut]
print(my_round(sum(my_scores) / len(my_scores)))

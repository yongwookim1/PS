from itertools import combinations

k = int(input())

for i in range(k):
    scores = list(map(int, input().split()))
    n = scores[0]
    scores = scores[1:]
    scores.sort()
    gaps = []
    for j in range(n - 1):
        gaps.append(scores[j + 1] - scores[j])
    print(f"Class {i+1}")
    print(f"Max {max(scores)}, Min {min(scores)}, Largest gap {max(gaps)}")

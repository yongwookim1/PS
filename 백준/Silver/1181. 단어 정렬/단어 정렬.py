import sys
input = sys.stdin.readline

n = int(input())
word_list = list(set([input().rstrip() for _ in range(n)]))

word_list.sort(key=lambda x:[len(x), x])

for i in word_list:
    print(i)
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

list1 = []
list2 = []
for i in range(n):
    list1.append(input().rstrip())
for j in range(m):
    list2.append(input().rstrip())

set = sorted(set(list1)&set(list2))
print(len(set))
for k in set:
    print(k)
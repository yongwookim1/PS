import sys
input = sys.stdin.readline

tree_list = dict()
st = 0
while True:
    tree = input().rstrip()
    if tree == '':
        break
    if tree not in tree_list:
        tree_list[tree] = 1
    else:
        tree_list[tree] += 1
    st += 1

new_list = []
for k, v in zip(tree_list.keys(), tree_list.values()):
    new_list.append([k,v])
new_list.sort()
# for k, v in zip(tree_list.keys(), tree_list.values()):
#     print(f'{k} {v/st*100:.4f}')
for k1, v1 in new_list:
    print(f'{k1} {v1/st*100:.4f}')
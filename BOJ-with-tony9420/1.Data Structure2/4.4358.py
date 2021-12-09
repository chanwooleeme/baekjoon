import sys

def input():
    return sys.stdin.readline().rstrip()

cnt = 0
tree_dict = {}
while True:
    tree = input()
    if not tree:
        break
    if tree in tree_dict:
        tree_dict[tree] += 1
    else:
        tree_dict[tree] = 1
    cnt += 1

tree_list = list(tree_dict.keys())
tree_list.sort()
for tree in tree_list:
    print('%s %.4f' %(tree, tree_dict[tree]/cnt*100))
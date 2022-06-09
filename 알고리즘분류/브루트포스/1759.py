from itertools import combinations

def valid(li: list):
    alpha = ['a', 'e', 'i', 'o', 'u']
    cnt = 0 
    for item in li:
        if item in alpha:
            cnt += 1
    if 1 <= cnt <= len(li) - 2:
        return True
    return False

L, C  = map(int, input().split())
pw = input().split()
pw.sort()

for item in list(combinations(pw, L)):
    if valid(item):
        print(''.join(item))
        
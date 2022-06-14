import sys

def input():
    return sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    n = int(input())
    wear_map = {}
    for _ in range(n):
        wear, type = input().split()
        if not type in wear_map:
            wear_map[type] = [wear]
        else:
            wear_map[type].append(wear)
    result = 1
    for k in wear_map:
        result *= (len(wear_map[k]) + 1)
    print(result - 1)
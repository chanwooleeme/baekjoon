import sys
from itertools import permutations
import itertools

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())

data = list(map(int, input().split()))
result = permutations(data, M)
result = list(set(result))
result.sort()
for item in result:
    for i in item:
        print(i, end=' ')
    print()
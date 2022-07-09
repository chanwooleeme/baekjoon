from itertools import permutations

N, M = map(int, input().split())
arr = list(map(int, input().split()))

result = sorted(set(permutations(arr, M)))

for item in result:
    print(' '.join(str(x) for x in item))
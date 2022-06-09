from itertools import combinations

N, S = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
for i in range(1,N+1):
    for item in tuple(combinations(arr, i)):
        if sum(item) == S:
            result += 1

print(result)
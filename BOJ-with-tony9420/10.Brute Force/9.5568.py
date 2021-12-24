import itertools

n = int(input())
k = int(input())

data =[]
for _ in range(n):
    data.append(input())

print(len(set(list(map(''.join, itertools.permutations(data, k))))))
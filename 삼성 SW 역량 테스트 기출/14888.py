import sys

input = sys.stdin.readline

def dfs(cnt):
    global max_v, min_v
    if cnt == N-1:
        total = arr[0]
        for i in range(1, N):
            op = permutations[i-1]
            if op == 0:
                total += arr[i]
            elif op == 1:
                total -= arr[i]
            elif op == 2:
                total *= arr[i]
            elif op == 3:
                total = int(total / arr[i])
        max_v = max(total, max_v)
        min_v = min(total, min_v)
        return
                
    for i in range(4):
        if oprs[i]:
            oprs[i] -= 1
            permutations.append(i)
            dfs(cnt + 1)
            permutations.pop()
            oprs[i] += 1

N = int(input())
arr = list(map(int, input().split()))
oprs = list(map(int, input().split()))
permutations = []
max_v, min_v = -1e9, 1e9
dfs(0)
print(max_v)
print(min_v)
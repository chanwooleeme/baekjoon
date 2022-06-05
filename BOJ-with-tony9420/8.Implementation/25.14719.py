import sys

def input():
    return sys.stdin.readline().rstrip()

H, W = map(int, input().split())
blocks = list(map(int, input().split()))
result = 0

for i in range(1, W - 1):
    max_left = max(blocks[:i+1])
    max_right = max(blocks[i:])
    result += min(max_left, max_right) - blocks[i]

print(result)
from audioop import reverse
import sys

def input():
    return sys.stdin.readline().rstrip()

N, K = map(int, input().split())
arr = [int(input())for _ in range(N)]
arr = list(reversed(arr))

result = 0
for item in arr:
    result += K // item
    K %= item
print(result)
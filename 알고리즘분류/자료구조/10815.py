import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
cards = set(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))
print(' '.join(map(lambda x: "1" if x in cards else "0", arr)))

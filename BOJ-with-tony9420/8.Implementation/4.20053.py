import sys
def input():
    return sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    li = []
    N = int(input())
    li = list(map(int, input().split()))
    result = str(min(li)) + " " + str(max(li))
    print(result)
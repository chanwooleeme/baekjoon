import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int, input().split()))
stack = [0]

for i in range(1, N):
    while stack and arr[stack[-1]] < arr[i]:
        arr[stack.pop()] = arr[i]
    stack.append(i)
    
while stack:
    arr[stack.pop()] = -1

print(*arr)
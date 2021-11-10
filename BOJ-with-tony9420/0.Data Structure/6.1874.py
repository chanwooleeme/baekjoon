import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
stack = [0]
idx = 1
result = str()
for _ in range(N):
    n = int(input())
    if stack[-1] < n:
        while stack[-1] != n:
            stack.append(idx)
            result += '+\n'
            idx += 1
    elif stack[-1] > n:
        if idx > n:
            print("NO")
            sys.exit(0)
        while stack[-1] != n:
            result += '-\n'
            stack.pop()
    if stack[-1] == n:
        result += '-\n'
        stack.pop()
print(result)
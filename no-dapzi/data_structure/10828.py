import sys

def input():
    return sys.stdin.readline().rstrip()

def solution():
    N = int(input())
    arr = []

    for _ in range(N):
        oprs = input().split()
        
        if oprs[0] == 'push':
            arr.append(int(oprs[1]))
        else:
            if not arr:
                if oprs[0] == 'empty':
                    print(1)
                elif oprs[0] == 'size':
                    print(0)
                else:
                    print(-1)
            else:
                if oprs[0] == 'empty':
                    print(0)
                elif oprs[0] == 'pop':
                    print(arr.pop())
                elif oprs[0] == 'size':
                    print(len(arr))
                elif oprs[0] == 'top':
                    print(arr[-1])

solution()
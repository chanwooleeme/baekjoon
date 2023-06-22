import sys


def input():
    return sys.stdin.readline().rstrip()


if __name__ == '__main__':
    N = int(input())
    stk = []
    result = 0
    for _ in range(N):
        x, y = map(int, input().split())
        if not stk:
            stk.append(y)
            continue
    
        while stk and stk[-1] > y:
            result += 1
            stk.pop()
        
        if not stk or (stk and y != stk[-1]):
            stk.append(y)
    
    while stk:
        if stk[-1] > 0:
            result += 1
        stk.pop()
    print(result)
    
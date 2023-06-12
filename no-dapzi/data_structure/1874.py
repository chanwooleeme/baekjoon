import sys


def input():
    return sys.stdin.readline().rstrip()

if __name__ == '__main__':
    N = int(input())
    stack = []
    result = []
    flag = False
    top = 1
    last = 1
    for i in range(N):
        n = int(input())
        while last <= n:
            stack.append(last)
            result.append("+")
            last += 1
        if n < stack[-1]:
            flag = True
            break
        else:
            stack.pop()
            result.append("-")

    if flag:
        print("NO")
    else:
        print('\n'.join(result))
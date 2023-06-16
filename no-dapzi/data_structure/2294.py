import sys


def input():
    return sys.stdin.readline().rstrip()


if __name__ == '__main__':
    n = int(input())
    ranges = []
    for i in range(n):
        x, r = map(int, input().split())
        ranges.append((x-r, i))
        ranges.append((x+r, i))
    ranges.sort()

    stack = []

    for range in ranges:
        if stack:
            if range[1] == stack[-1][1]:
                stack.pop()
            else:
                stack.append(range)
        else:
            stack.append(range)

    if stack:
        print("NO")
    else:
        print("YES")

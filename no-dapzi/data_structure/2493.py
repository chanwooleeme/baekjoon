import sys


def input():
    return sys.stdin.readline().rstrip()


if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))
    stack = []
    result = []
    for idx, num in enumerate(nums):
        while stack:
            if stack[-1][1] > num:
                result.append(stack[-1][0] + 1)
                break
            else:
                stack.pop()
        if not stack:
            result.append(0)
        stack.append([idx, num])

    print(" ".join(map(str, result)))

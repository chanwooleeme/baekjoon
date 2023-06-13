import sys


def input():
    return sys.stdin.readline().rstrip()


if __name__ == '__main__':
    s = input()
    stack = []
    result = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append('(')
        if s[i] == ')':
            if s[i-1] == '(':
                stack.pop()
                result += len(stack)
            else:
                stack.pop()
                result += 1
    print(result)

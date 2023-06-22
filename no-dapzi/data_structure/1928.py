import sys


def input():
    return sys.stdin.readline().rstrip()


if __name__ == '__main__':
    s = input()
    stack = []
    result = ""
    for idx, val in enumerate(s):
        if val.isalpha():
            result += val
        elif val == '(':
            stack.append(val)
        elif val == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()
        else:
            if val == '*' or val == '/':
                while stack and (stack[-1] == '*' or stack[-1] == '/'):
                    result += stack.pop()
                stack.append(val)
            else:
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.append(val)
    
    while stack:
        result += stack.pop()
    print(result)

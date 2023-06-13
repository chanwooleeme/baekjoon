import sys

def input():
    return sys.stdin.readline().rstrip()



def valid_stack(stack: list, cur_chr: chr):
    if cur_chr == ')':
        mul = 2
        tmp = 0
        while stack:
            if stack[-1] == '(':
                stack.pop()
                stack.append(tmp * mul)
                break
            elif stack[-1] == '[':
                return False
            else:
                tmp += stack.pop()
    else:
        mul = 3
        tmp = 0
        while stack:
            if stack[-1] == '[':
                stack.pop()
                stack.append(tmp * mul)
                break
            elif stack[-1] == '(':
                return False
            else:
                tmp += stack.pop()
    return stack


def cal_stack(s: str):
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append('(')
        elif s[i] == '[':
            stack.append('[')
        elif s[i] == ')':
            if not stack:
                print("0")
                return
            if stack[-1] == '(':
                stack.pop()
                stack.append(2)
            else:
                stack = valid_stack(stack, s[i])
                if not stack:
                    print("0")
                    return
        elif s[i] == ']':
            if not stack:
                print("0")
                return
            if stack[-1] == '[':
                stack.pop()
                stack.append(3)
            else:
                stack = valid_stack(stack, s[i])
                if not stack:
                    print("0")
                    return
    for i in range(len(stack)):
        if not str(stack[i]).isdigit():
            print("0")
            return
    print(sum(stack))


if __name__ == '__main__':
    s = input()
    cal_stack(s)
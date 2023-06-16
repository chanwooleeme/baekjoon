import sys

def input():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    while True:
        s = input()
        if s == '.':
            break
        stack = []
        flag = False
        for i in range(len(s)):
            if s[i] == '(':
                stack.append('(')
            elif s[i] == ')':
                if stack:
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        flag = True
                else:
                    flag = True
                    break
            elif s[i] == '[':
                stack.append('[')
            elif s[i] == ']':
                if stack:
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        flag = True
                else:
                    flag = True
                    break
        if flag or stack:
            print("no")
        else:
            print("yes")

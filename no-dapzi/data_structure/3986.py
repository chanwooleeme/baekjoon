import sys

def input():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    N = int(input())
    result = 0
    for _ in range(N):
        s = input()
        stack = []
        for i in range(len(s)):
            if not stack:
                stack.append(s[i])
            else:
                if s[i] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(s[i])
        if not stack:
            result += 1
    print(result)

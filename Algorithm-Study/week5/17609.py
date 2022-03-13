import sys

def input():
    return sys.stdin.readline().rstrip()

def check(s, left, right):
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            check1 = pseudo(s, left + 1, right)
            check2 = pseudo(s, left, right - 1)
            if check1 or check2:
                return 1
            else:
                return 2
    return 0

def pseudo(s, left, right):
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

T = int(input())

for _ in range(T):
    s = input()
    print(check(s, 0, len(s)-1))
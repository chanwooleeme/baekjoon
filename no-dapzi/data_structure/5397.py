import sys


def input():
    return sys.stdin.readline().rstrip()


if __name__ == '__main__':
    N = int(input())
    for _ in range(N):
        l_stk = []
        r_stk = []
        s = input()
        for i in range(len(s)):
            if s[i] == '<':
                if l_stk:
                    r_stk.append(l_stk.pop())
            elif s[i] == '>':
                if r_stk:
                    l_stk.append(r_stk.pop())
            elif s[i] == '-':
                if l_stk:
                    l_stk.pop()
            else:
                l_stk.append(s[i])
        
        l_stk.extend(reversed(r_stk))
        print(''.join(l_stk))

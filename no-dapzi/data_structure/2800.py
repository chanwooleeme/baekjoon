import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def find_pairs(s):
    stack = []
    pairs = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        elif s[i] == ')':
            idx = stack.pop()
            pairs.append([idx, i])
    return pairs


def bfs(s: str):
    q = deque()
    result_sets = set()
    q.append(s)
    while q:
        cur = q.pop()
        pairs = find_pairs(cur)
        for pair in pairs:
            tmp = cur
            front, rear = pair
            tmp = tmp[:rear] + tmp[rear+1:]
            tmp = tmp[:front] + tmp[front+1:]
            if not tmp in result_sets:
                result_sets.add(tmp)
                q.append(tmp)
            else:
                continue
    return list(result_sets)


if __name__== '__main__':
    s = input()
    result = bfs(s)
    result.sort()
    print('\n'.join(result))

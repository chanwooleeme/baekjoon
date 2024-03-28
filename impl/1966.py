import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        q = deque([])
        inputs = list(map(int, input().split()))
        priority = list()
        for i in range(len(inputs)):
            q.append([inputs[i], i])
            priority.append(inputs[i])
        priority = sorted(priority)
        cnt = 0
        while q:
            cur = q.popleft()

            if cur[0] == priority[-1]:
                cnt += 1
                priority.pop()
                if cur[1] == M:
                    break
            else:
                q.append(cur)
        print(cnt)

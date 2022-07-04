from collections import deque

def solution(priorities, location):
    q = deque([v, i] for i, v in enumerate(priorities))
    cnt = 1
    while len(q):
        item = q.popleft()
        if q and max(q)[0] > item[0]:
            q.append(item)
        else:
            if item[1] == location:
                return cnt
            else:
                cnt += 1

print(solution([2,1,3,2], 2))
print(solution([1, 1, 9, 1, 1, 1]	, 0))
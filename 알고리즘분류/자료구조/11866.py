from collections import deque

N, K = map(int, input().split())

q = deque([i for i in range(1, N + 1)])
result = []
while q:
    q.rotate(-(K-1))
    result.append(q.popleft())
    
print(str(result).replace('[', '<').replace(']', '>'))
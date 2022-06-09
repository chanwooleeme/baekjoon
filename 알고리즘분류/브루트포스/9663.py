
import sys

sys.setrecursionlimit(10**9)
def is_promising(x):
    for i in range(x):
        if board[x] == board[i] or abs(board[x] - board[i]) == abs(x - i):
            return False
    return True

def dfs(x):
    global result
    if x == N:
        result += 1
        return
    
    for i in range(N):
        board[x] = i
        if is_promising(x):
            dfs(x + 1)

N = int(input())
board = [0] * N
result = 0
dfs(0)
print(result)
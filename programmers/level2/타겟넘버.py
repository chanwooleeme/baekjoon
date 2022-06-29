
def dfs(n, cnt, numbers):
    global answer, t
    if n == len(numbers):
        if cnt == t:
            answer += 1
        return
    dfs(n + 1, cnt + numbers[n], numbers)
    dfs(n + 1, cnt - numbers[n], numbers)
    
def solution(numbers, target):
    global answer, t
    t = target
    answer = 0
    dfs(0, 0, numbers)
    return answer


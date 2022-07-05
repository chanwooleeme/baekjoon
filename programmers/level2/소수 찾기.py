def isPrime():
    _MAX = 10000000
    arr = [False, False] + [True] * (_MAX - 1)
    visited = [False] * _MAX
    for i in range(2, _MAX+1):
        if arr[i]:
            for j in range(2*i, _MAX+1, i):
                arr[j] = False
    return arr, visited

def solution(numbers):
    answer = 0
    arr, visited = isPrime()
    from itertools import permutations
    for i in range(len(numbers)):
        for nums in permutations(numbers, i+1):
            s = ""
            for num in nums:
                s += num
            
            if arr[int(s)] and not visited[int(s)]:
                answer += 1
                visited[int(s)] = True
    return answer
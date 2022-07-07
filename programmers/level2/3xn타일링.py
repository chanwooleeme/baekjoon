def solution(n):
    if n % 2 == 1:
        return 0
    arr = [0,0,3,0,11,0]
    if n < 5:
        return arr[n]
    arr += [0] * ((n-5))
    
    for i in range(6, n + 1):
        if i % 2 == 0:
            arr[i] = (arr[i-2] * 4 - arr[i-4]) % 1000000007
    return arr[n]
def solution(arr, n):
    global result
    if not arr:
        return
    _min = min(arr)
    idx = arr.index(_min)
    result[n + idx] = _min
    print("".join(result))
    solution(arr[idx + 1:], n + idx + 1)
    solution(arr[:idx], n)
    
s = list(input().rstrip())
result = [""] * len(s)
solution(s, 0)
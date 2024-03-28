from itertools import combinations

def list_to_int(arr):
    cnt = 0
    mul = 1
    while arr:
        cnt += arr.pop() * mul
        mul *= 10
    return cnt

def int_to_list(n):
    tmp = n
    arr = []
    while tmp:
        arr.append(tmp % 10)
        tmp //= 10
    return list(reversed(arr))

def split_three_part(arr):
    comb = [i for i in range(1, len(arr))]
    return list(combinations(comb, 2))

def count_odd_in_list(arr):
    cnt = 0
    for item in arr:
        if item % 2 == 1:
            cnt += 1
    return cnt

def dfs(li, n):
    global min_result, max_result
    if len(li) == 1:
        max_result = max(max_result, n)
        min_result = min(min_result, n)
    if len(li) >= 3:
        for item in split_three_part(li):
            _sum = list_to_int(li[:item[0]]) + list_to_int(li[item[0]:item[1]]) + list_to_int(li[item[1]:]) #92
            _sum_list = int_to_list(_sum) #[9, 2]
            dfs(_sum_list, n + count_odd_in_list(_sum_list))
    elif len(li) == 2:
        _list = int_to_list(li[0] + li[1])
        dfs(_list, n + count_odd_in_list(_list))
        
N = int(input())
min_result, max_result = 1e9, -1
li = int_to_list(N)
dfs(li, count_odd_in_list(li))
print(min_result, max_result)
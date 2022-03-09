def win(t):
    if t == 0 or t == 1:
        return 6
    elif t == 2:
        return 5
    elif t == 3:
        return 4
    elif t == 4:
        return 3
    elif t == 5:
        return 2
    elif t == 6:
        return 1
        
def solution(lottos, win_nums):
    answer = []
    cnt = 0
    zero_cnt = 0
    for num in lottos:
        if num in win_nums:
            cnt += 1
        if num == 0:
            zero_cnt += 1
            
    answer.append(win(cnt + zero_cnt))
    answer.append(win(cnt))
    
    return answer
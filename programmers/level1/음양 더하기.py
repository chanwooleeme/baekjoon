def solution(absolutes, signs):
    answer = 0
    for idx, sign in enumerate(signs):
        if sign:
            signs[idx] = 1
        else:
            signs[idx] = -1
    for i in range(len(absolutes)):
        answer += (absolutes[i] * signs[i])
    return answer
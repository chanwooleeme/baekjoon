def solution(numbers, hand):
    answer = ''
    
    l_recent = 10
    r_recent = 11
    pad = [
        (3, 1), 
        (0, 0), (0, 1), (0, 2),
        (1, 0), (1, 1), (1, 2),
        (2, 0), (2, 1), (2, 2),
        (3, 0), (3, 2)
    ]
    
    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            l_recent = number
        elif number in [3, 6, 9]:
            answer += 'R'
            r_recent = number
        else:
            nx, ny = pad[number]
            lx, ly = pad[l_recent]
            rx, ry = pad[r_recent]
            if abs(nx - lx) + abs(ny - ly) > abs(nx - rx) + abs(ny -ry):
                answer += 'R'
                r_recent = number
            elif abs(nx - lx) + abs(ny - ly) < abs(nx - rx) + abs(ny -ry) :
                answer += 'L'
                l_recent = number
            else:
                if hand == "right":
                    answer += 'R'
                    r_recent = number
                else:
                    answer += 'L'
                    l_recent = number
    return answer
def decimal_to_124(n):
    result = ""
    while n:
        if n % 3 == 0:
            result += "4"
            n = n // 3 - 1
        else:
            result += str(n % 3)
            n //= 3
    return result[::-1]

def solution(n):
    return decimal_to_124(n)


solution(1)
solution(2)
solution(3)
solution(4)    
solution(5)
solution(6)
solution(7)
solution(8)
solution(9)
solution(10)
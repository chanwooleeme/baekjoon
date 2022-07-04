def solution(phone_book):
    _dict = {}
    for item in phone_book:
        _dict[item] = 0
    
    for key in _dict.keys():
        for i in range(1, len(key)+1):
            print(key[:i])
            if key[:i] in _dict:
                _dict[key[:i]] += 1
                if _dict[key[:i]] == 2:
                    return False
    return True

solution(["123", "456", "789"])
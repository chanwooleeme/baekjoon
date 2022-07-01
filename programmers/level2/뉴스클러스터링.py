import math

def jhakhad(a:dict, b:dict):
    if not a and not b:
        return 1
    gyo = 0
    hap = 0
    for key in a.keys():
        if key in b.keys():
            gyo += min(a[key], b[key])
        hap += a[key]
    for key in b.keys():
        hap += b[key]
    return gyo / (hap - gyo)

def split(s):
    _dict = dict()
    _set = set()
    for i in range(len(s) - 1):
        if s[i].isalpha() and s[i+1].isalpha():
            _str = s[i] + s[i+1]
            if _str in _dict:
                _dict[_str] += 1
            else:
                _dict[_str] = 1
                
    return _dict
        
def solution(str1, str2):
    return math.trunc(jhakhad(split(str1.upper()),split(str2.upper())) * 65536)
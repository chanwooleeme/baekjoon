import sys

def input():
    return sys.stdin.readline().rstrip()


def palindrom(s: str):
    return


if __name__ == '__main__':
    s = input()
    word_count = dict()
    cache = set()
    result = ['0'] * len(s)
    front, rear =  0, len(s)-1
    for c in s:
        if c in word_count:
            word_count[c] += 1
        else:
            word_count[c] = 1
        cache.add(c)
    
    cache = sorted(cache)
    for c in cache:
        while word_count[c] != 0:
            if word_count[c] % 2 == 0:
                if front <= rear:
                    result[front] = c
                    result[rear] = c
                    front += 1
                    rear -= 1
                    word_count[c] -= 2
            else:
                result[len(s) // 2] = c
                word_count[c] -= 1
    
    if '0' in set(result):
        print("I'm Sorry Hansoo")
    else:
        print(''.join(result))
            
    
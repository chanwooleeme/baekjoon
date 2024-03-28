import sys

def input():
    return sys.stdin.readline().rstrip()

if __name__ == '__main__':
    while True:
        s = input()
        if s == '*':
            break

        result = True
        l = len(s)
        word_set = set()
    
        if l - 2 <= 0:
            result = True
        else:
            for i in range(l-1):
                word_set = set()
                for j in range(l-i-1):
                    word_set.add(s[j] + s[j+i+1])
                
                # if len(word_set) != l-1-i:
                #     result = False
                #     print(word_set)
        if result == False:
            print(s + ' is NOT surprising')
        else:
            print(s + ' is surprising')

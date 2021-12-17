N = int(input())
size = 4 * N - 3
_map = [[' '] * size for _ in range(size)]
    
def draw(n, p):
    if n == 1:
        _map[p][p] = '*'
        return
    d = 4 * n - 3
    for i in range(p, p + d):
        for j in range(p, p + d):
            _map[i][j] = '*'
    for i in range(p + 1, p + d - 1):
        for j in range(p + 1, p + d - 1):
            _map[i][j] = ' '
    return draw(n - 1, p + 2)

draw(N, 0)

for i in range(size):
    result = []
    for j in range(size):
        result.append(str(_map[i][j]))
    print(" ".join(result))
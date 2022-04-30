import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

tet_line = [
    [[0, 0], [0, 1], [0, 2], [0, 3]], 
    [[0, 0], [1, 0], [2, 0], [3, 0]]
]

tet_square = [
    [[0, 0], [0, 1], [1, 0], [1, 1]]
    ]

tet_L = [
    [[0, 0], [1, 0], [2, 0], [2, 1]],
    [[0, 0], [0, 1], [0, 2], [1, 0]],
    [[0, 0], [0, 1], [1, 1], [2, 1]],
    [[0, 2], [1, 0], [1, 1,],[1, 2]],
    [[0, 1], [1, 1], [2, 0], [2, 1]],
    [[0, 0], [1, 0], [1, 1], [1, 2]],
    [[0, 0], [0, 1], [1, 0], [2, 0]],
    [[0, 0], [0, 1], [0, 2], [1, 2]]
    ]

tet_jigzag = [
    [[0, 0], [1, 0], [1, 1], [2, 1]],
    [[0, 1], [0, 2], [1, 0], [1, 1]],
    [[0, 1], [1, 0], [1, 1], [2, 0]],
    [[0, 0], [0, 1], [1, 1], [1, 2]]
]

tet_bolok = [
    [[0, 0], [0, 1], [0, 2], [1, 1]],
    [[0, 1], [1, 0], [1, 1], [2, 1]],
    [[0, 1], [1, 0], [1, 1], [1, 2]],
    [[0, 0], [1, 0], [1, 1], [2, 0]]
]

tet_family = [tet_line, tet_square, tet_L, tet_jigzag, tet_bolok]

result = 0
for i in range(N):
    for j in range(M):
        for tet in tet_family:
            for shape in tet:
                tet_val = 0
                for d in shape:
                    x, y = i + d[0], j + d[1]
                    if x < 0 or y < 0 or x >= N or y >= M:
                        continue
                    tet_val += arr[x][y]
                result = max(result, tet_val)

print(result)
        
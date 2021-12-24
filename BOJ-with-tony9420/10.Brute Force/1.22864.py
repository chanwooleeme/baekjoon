A, B, C, M = map(int, input().split())
stress = 0
process = 0
for _ in range(24):
    if stress + A <= M:
        stress += A
        process += B
    else:
        stress -= C
        if stress < 0:
        	stress = 0
print(process)
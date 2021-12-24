A = int(input())
T = int(input())
data = int(input())

bun = []
daegi = []
i = 2
idx = 0
while True:
    bun.append(idx % A)
    idx += 1
    daegi.append(idx % A)
    idx += 1
    bun.append(idx % A)
    idx += 1
    daegi.append(idx % A)
    idx += 1
    for j in range(i):
        bun.append(idx % A)
        idx += 1
    for j in range(i):
        daegi.append(idx % A)
        idx += 1
    i += 1
    if len(bun) > T:
        break
if data == 0:
    print(bun[T - 1] % A)
else:
    print(daegi[T - 1] % A)
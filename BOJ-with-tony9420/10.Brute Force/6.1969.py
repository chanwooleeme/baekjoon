N, M = map(int, input().split())
data = []
for _ in range(N):
    data.append(list(input()))
hd = 0
result = ""
for i in range(M):
    dna = {'A': 0, 'C': 0,  'G': 0, 'T': 0}
    for j in range(N):
        dna[str(data[j][i])] += 1
    max_key = max(dna, key=dna.get)
    max_val = max(dna.values())
    hd += (N - max_val)
    result += max_key
print(result)
print(hd)
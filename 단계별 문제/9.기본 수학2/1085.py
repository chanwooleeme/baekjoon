x, y, w, h = map(int, input().split())
a = abs(w - x)
b = abs(h - y)
print(min(min(a, x), min(b, y)))
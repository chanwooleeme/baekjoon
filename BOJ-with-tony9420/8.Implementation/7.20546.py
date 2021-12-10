import sys
        
def input():
    return sys.stdin.readline().rstrip()

amount = int(input())
chart = list(map(int, input().split()))

J_amount = amount
J_stock = 0 #몇주
for price in chart:
    tmp = J_amount // price
    if tmp > 0:
        J_stock += tmp
        J_amount -= tmp * price
        
S_amount = amount
S_stock = 0 #몇주
buy = 0
sell = 0
for i in range(1, len(chart)):
    if chart[i -1] < chart[i] and S_stock > 0:
        sell += 1
        buy = 0
    elif chart[i - 1] > chart[i]:
        buy += 1
        sell = 0
    if buy >= 3 and S_amount >= chart[i]:
        tmp = S_amount // chart[i]
        S_stock += tmp
        S_amount -= tmp * chart[i]
    elif sell >= 3 and S_stock > 0:
        S_amount += chart[i] * S_stock
        S_stock = 0
S = S_amount + S_stock * chart[-1]
J = J_amount + J_stock * chart[-1]
if S < J:
    print("BNP")
elif S > J:
    print("TIMING")
else:
    print("SAMESAME")
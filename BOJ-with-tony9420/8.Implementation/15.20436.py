l_keyboard_init = [list("qwert"), list("asdfg"), list("zxcv")]
r_keyboard_init = [list(" yuiop"), list(" hjkl "), list("bnm   ")]
l_keyboard = {}
r_keyboard = {}
for i in range(len(l_keyboard_init)):
    for j in range(len(l_keyboard_init[i])):
        l_keyboard[l_keyboard_init[i][j]] = [i, j]

for i in range(len(r_keyboard_init)):
    for j in range(len(r_keyboard_init[i])):
        r_keyboard[r_keyboard_init[i][j]] = [i, j]
        
def distance(finger, keyboard, goal):
    x, y = keyboard[finger]
    goal_x, goal_y = keyboard[goal]
    distance = int((((x - goal_x) ** 2) ** 0.5) + (((y - goal_y) ** 2) ** 0.5))
    return distance
        
l, r = input().split()
s = input()
cnt = 0
for item in s:
    if item in l_keyboard:
        cnt += distance(l, l_keyboard, item) + 1
        l = item
    else:
        cnt += distance(r, r_keyboard, item) + 1
        r = item
        
print(cnt)
    
keyboard_init = [list("qwertyuiop"), list("asdfghjkl"), list("zxcvbnm")]
keyboard = {}
for i in range(len(keyboard_init)):
    for j in range(len(keyboard_init[i])):
        keyboard[keyboard_init[i][j]] = [i, j]
def distance(l, r, goal):
        lx, ly = keyboard[l]
        rx, ry = keyboard[r]
        goalx, goaly = keyboard[goal]
        l_distance = ((lx - goalx) ** 2 ** 0.5) + ((ly - goaly) ** 2 ** 0.5)
        print(l_distance)
        r_distance = ((rx - goalx) ** 2 ** 0.5) + ((ry - goaly) ** 2 ** 0.5)
        print(r_distance)
        if l_distance < r_distance:
            l = goal
            return r, l, r_distance
        else:
            r = goal
            return r, l, l_distance
        
l, r = input().split()
s = input()
cnt = 0
for item in s:
    l_tmp, r_tmp, cnt_tmp = distance(l, r, item)
    l = l_tmp
    r = r_tmp
    cnt += cnt_tmp + 1

print(cnt)
    
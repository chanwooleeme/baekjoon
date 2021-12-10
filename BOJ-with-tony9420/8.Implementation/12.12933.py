import sys

def input():
    return sys.stdin.readline().rstrip()

def exit():
    print(-1)
    sys.exit(0)

stack_list = []
S = input()
for item in S:
    if item == 'q':
        if not stack_list:
            stack_list.append(['q'])
        else:
            flag = False
            for stack in stack_list:
                if stack[-1] == 'k':
                    stack.append('q')
                    flag = True
                    break
            if not flag:
                stack_list.append(['q'])
    else:
        if not stack_list:
            exit()
        if item == 'u':
            flag = False
            for stack in stack_list:
                if stack[-1] == 'q':
                    stack.append('u')
                    flag = True
                    break
            if not flag:
                exit()
        elif item == 'a':
            flag = False
            for stack in stack_list:
                if stack[-1] == 'u':
                    stack.append('a')
                    flag = True
                    break
            if not flag:
                exit()
        elif item == 'c':
            flag = False
            for stack in stack_list:
                if stack[-1] == 'a':
                    stack.append('c')
                    flag = True
                    break
            if not flag:
                exit()
        elif item == 'k':
            flag = False
            for stack in stack_list:
                if stack[-1] == 'c':
                    stack.append('k')
                    flag = True
                    break
            if not flag:
                exit()
for stack in stack_list:
    if stack[-1] != 'k':
        print(-1)
        sys.exit(0)
else:
    print(len(stack_list))
import sys

sys.setrecursionlimit(10**9)

def in_order(node):
    global in_order_result
    
    if node.left:
        in_order(tree[node.left])
        
    in_order_result = node.data

    if node.right:
        in_order(tree[node.right])

def similar_in_order(node):
    global cnt

    if node.left:
        similar_in_order(tree[node.left])
        cnt += 1

    if node.data == in_order_result:
        print(cnt)
        exit(0)
    cnt += 1
            
    if node.right:
        similar_in_order(tree[node.right])
        cnt += 1

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
        
def input():
    return sys.stdin.readline().rstrip()        

N = int(input())
tree = {}

for _ in range(N):
    data, left, right = map(int, input().split())
    if left == -1: left = None
    if right == -1: right = None
    tree[data] = Node(data, left, right)

in_order_result = 0
in_order(tree[1])

cnt = 0
similar_in_order(tree[1])
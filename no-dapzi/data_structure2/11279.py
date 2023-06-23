import sys
import heapq


def input():
    return sys.stdin.readline().rstrip()


if __name__ == '__main__':
    N = int(input())
    heap = []
    for _ in range(N):
        n = int(input())
        if n == 0:
            if not heap:
                print("0")
            else:
                print(heapq.heappop(heap) * -1)
        else:
            heapq.heappush(heap, -n)
    
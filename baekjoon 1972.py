import sys
import heapq

min_heap = []

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())

    if n == 0:
        if len(min_heap):
            print(heapq.heappop(min_heap))
        else:
            print(0)
    else:
        heapq.heappush(min_heap, n)
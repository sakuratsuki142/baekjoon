import sys
t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    rank = list(map(int, sys.stdin.readline().strip().split()))
    
    result = 1
    while rank:
        if rank[0] < max(rank):
            rank.append(rank.pop(0))
        else:
            if m == 0:
                break
            rank.pop(0)
            result += 1

        if m > 0:
            m = m - 1
        else:
            m = len(rank) - 1

    print(result)

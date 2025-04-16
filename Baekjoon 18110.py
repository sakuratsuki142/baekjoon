import sys
n = int(sys.stdin.readline())
if (n == 0):
    print(0)
else:
    rank = []
    for i in range(n):
        rank.append(int(sys.stdin.readline()))
    rank.sort()
    avarage = n * 0.15
    if (avarage - int(avarage) >= 0.5):
        avarage = int(avarage) + 1
    else:
        avarage = int(avarage)
    sum = 0
    for j in range(avarage, n-avarage):
        sum += rank[j]
    final_rank = sum/(n-avarage*2)

    if (final_rank - int(final_rank) >= 0.5):
        print(int(final_rank) + 1)
    else:
        print(int(final_rank))

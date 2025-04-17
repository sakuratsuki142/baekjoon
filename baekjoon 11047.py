import sys
N, K = map(int, sys.stdin.readline().split())
money = []
for i in range(N):
    money.append(int(sys.stdin.readline()))
money.reverse()
count = 0
for j in money:
    count += K // j
    K = K % j
    if(K == 0):
        print(count)
        break
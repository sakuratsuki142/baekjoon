import sys
N = int(sys.stdin.readline())
minute = list(map(int, sys.stdin.readline().split()))
minute.sort()
sum_minute = 0
for j in range(len(minute)+1):
    sum_minute += sum(minute[:j])
print(sum_minute)
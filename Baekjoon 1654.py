#내가 했지만 시간초과가 난 코드
#import sys
#K, N = map(int, sys.stdin.readline().split())
#lines = []
#for i in range(K):
#    lines.append(int(sys.stdin.readline()))
#lines_sum = sum(lines)

#want_cm = lines_sum//N
#while (1):
#    count = 0
#    for j in lines:
#        while j > want_cm:
#            j = j - want_cm
#            count += 1
#    if(count >= N):
#        break
#        else:
#        want_cm -= 1
#print(want_cm)

import sys

K, N = map(int, sys.stdin.readline().strip().split())

lines = []
for _ in range(K):
    lines.append(int(sys.stdin.readline().strip()))

start, end = 1, max(lines)

while (start <= end):  # 이진탐색으로 중간값을 찾아 문제를 해결한다.
    mid = (start + end) // 2
    line_cnt = 0

    for line in lines:
        line_cnt += line // mid

    if line_cnt >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)
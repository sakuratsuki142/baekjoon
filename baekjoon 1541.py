import sys

arr = list(map(str, sys.stdin.readline().strip().split('-')))
answer = 0
for i in arr[0].split('+'):
  answer += int(i)

for i in arr[1:]:
  for j in i.split('+'):
    answer -= int(j)

print(answer)
import sys
n, m = map(int, sys.stdin.readline().split())
arr = [0]
arr += list(map(int, sys.stdin.readline().split()))

for i, num in enumerate(arr):
  if i>0:
    arr[i] = arr[i-1] + num

for _ in range(m):
  i,j = map(int, sys.stdin.readline().split())
  print(arr[j] - arr[i-1])
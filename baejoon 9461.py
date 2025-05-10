import sys
arr = [0, 1, 1, 1] + [0 for x in range(97)]

def func(x):
  if arr[x]:
    return arr[x]
  else:
    arr[x] = func(x-2) + func(x-3)
    return arr[x]

t = int(sys.stdin.readline())
for _ in range(t):
  n = int(sys.stdin.readline())
  print(func(n))
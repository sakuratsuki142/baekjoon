import sys
N = int(sys.stdin.readline())
succed = True
stack = []
A = []
count = 1
for i in range(N):
    B = int(sys.stdin.readline())
    while count <= B:
        stack.append(count)
        count += 1
        A.append('+')
    if (stack[-1] == B):
        stack.pop()
        A.append('-')
    else:
        succed = False
        break

if (succed == False):
    print('NO')
else:
    for j in A:
        print(j)
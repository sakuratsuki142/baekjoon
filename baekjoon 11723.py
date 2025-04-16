import sys
N = int(sys.stdin.readline())
stack = []
for i in range(N):
    order = list(map(str, sys.stdin.readline().strip().split()))
    if (order[0] == 'add'):
        stack.append(int(order[1]))
        S = set(stack)
        stack = list(S)
    elif (order[0] == 'check'):
        S = set(stack)
        if(int(order[1]) in S):
            print(1)
        else:
            print(0)
    elif (order[0] == 'remove'):
        S = set(stack)
        if(int(order[1]) in S):
            S.remove(int(order[1]))
            stack = list(S)
    elif (order[0] == 'toggle'):
        S = set(stack)
        if(int(order[1]) in S):
            S.remove(int(order[1]))
            stack = list(S)
        else:
            S.add(int(order[1]))
            stack = list(S)
    elif(order[0] == 'all'):
        stack = [j for j in range(1, 21)]
    elif(order[0] == 'empty'):
        stack = []
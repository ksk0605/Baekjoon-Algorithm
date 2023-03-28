from sys import stdin

n = int(input()) 
stack = [0] * 200001

result = 0
for _ in range(n): 
    personId, inout = map(int, stdin.readline().split())
    if (inout == 1) : 
        if stack[personId] == 1:
            result += 1
        else: 
            stack[personId] += 1
    else: 
        if stack[personId] == 0:
            result += 1
        else: 
            stack[personId] -= 1

print(result+ sum(stack))
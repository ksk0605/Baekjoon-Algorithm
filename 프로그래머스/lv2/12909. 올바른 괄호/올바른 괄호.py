from collections import deque

def solution(s):
    answer = True
    stack = deque([])
    s = deque(s)
    
    while s: 
        gh = s.popleft()
        if len(stack) == 0 and gh == ')': 
            return False
        
        if gh == ')':
            stack.pop()
        else : 
            stack.append(gh)
    
    print(stack)
    
    if len(stack) == 0:
        return True
    else: 
        return False

# 조건 1 무조건 왼쪽 괄호가 먼저 와야한다. -> 스택이 비어있는데 닫는 괄호가 나오면 false
# 조건 2 오른쪽 괄호는 왼쪽 괄호와 개수가 똑같아야 한다. -> 스택에 개수가 남아있으면 false

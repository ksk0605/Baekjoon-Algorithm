from collections import deque 

def solution(arr):
    
    dq = deque([-1])
    
    for item in arr: 
        if item != dq[-1]:
            dq.append(item)
    return list(dq)[1:]
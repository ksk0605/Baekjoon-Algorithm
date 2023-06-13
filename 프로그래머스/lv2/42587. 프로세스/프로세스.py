from collections import deque as dq

def solution(priorities, location):
    target_queue = [False] * len(priorities)
    target_queue[location] = True
    
    tq = dq(target_queue)
    pq = dq(priorities)
    
    cnt = 1
    
    while True: 
        check = False
        p = pq.popleft() 
        t = tq.popleft()
        for i in range(len(pq)): 
            if p < pq[i]: 
                pq.append(p)
                tq.append(t)
                check = True
                break
    
        if check:
            continue
        else: 
            if t == True: 
                return cnt
            else: 
                cnt += 1 
                continue

# 바라보는 프로세스의 위치가 계속 바뀜 
# pop 될때 순서가 늘어남

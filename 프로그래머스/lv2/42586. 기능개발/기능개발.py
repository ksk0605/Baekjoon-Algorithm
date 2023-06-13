from collections import deque
def solution(progresses, speeds):
    
    answer = []
    
    progresses = deque(progresses)
    speeds = deque(speeds)
    while progresses: 
        
        for i in range(len(speeds)): 
            progresses[i] += speeds[i]
        
        fin = 0
        
        while progresses[0] >= 100: 
            progresses.popleft()
            speeds.popleft()
            fin+=1 
            if len(progresses) == 0:
                break
        
        if fin > 0: 
            answer.append(fin)
            
    return answer
# 완료되는 시점? 완료여부 
# 완료된 것들은 한번에 나가야 함. 
# 시점은 필요없음
# 매번 반복마다 progresses에 speed 더해주기 
# 반복의 끝에 100이 넘은 만큼 pop  개수를 answer에 저장 
# O(n * n)

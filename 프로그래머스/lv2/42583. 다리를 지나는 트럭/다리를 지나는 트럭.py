from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_len = len(truck_weights)
    fin_trucks = 0
    time_cnt =  0
    
    truck_weights = deque(truck_weights)
    bridge_trucks = deque([])
    bridge_times = deque([])
    
    while truck_len != fin_trucks: 
        
        if bridge_times and bridge_times[0] == bridge_length + 1: 
            bridge_trucks.popleft() 
            bridge_times.popleft()
            fin_trucks += 1
        
        if len(truck_weights) != 0 and (sum(bridge_trucks) + truck_weights[0] <= weight): 
            t = truck_weights.popleft()
            bridge_trucks.append(t)
            bridge_times.append(1)
        
        
        
        for i in range(len(bridge_times)):
            bridge_times[i] += 1
        
        
        time_cnt += 1
        
    return time_cnt
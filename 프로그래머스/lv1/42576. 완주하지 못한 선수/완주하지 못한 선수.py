def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)): 
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]
#     dic = {}
#     for i in participant: 
#         if i in dic: 
#             dic[i] += 1
#         else:
#             dic[i] = 1

    
#     for i in completion: 
#         dic[i] -= 1
    
#     for i in dic: 
#         if dic[i] > 0: 
#             return i
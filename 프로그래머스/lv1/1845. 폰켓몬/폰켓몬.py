def solution(nums):
    
    ponks = set()
    
    for i in nums: 
        ponks.add(i)
    
    answer = len(ponks)
    return min(answer,len(nums)/2)
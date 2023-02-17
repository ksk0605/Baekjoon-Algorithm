def solution(sizes):
    maxArr = []
    minArr = []
    for i in sizes: 
        maxArr.append(max(i))
        minArr.append(min(i))
    
    answer = max(maxArr) * max(minArr)
    return answer
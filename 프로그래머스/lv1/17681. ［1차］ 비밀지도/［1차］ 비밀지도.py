def solution(n, arr1, arr2):
    lines = []
    for i in range(n): 
        lines.append(bin(arr1[i] | arr2[i])[2:].zfill(n))

                
    answer = []
    for line in lines:
        new_line = line.replace('0', ' ')
        new_line  = new_line.replace('1', '#')
        answer.append(new_line)
    
    return answer
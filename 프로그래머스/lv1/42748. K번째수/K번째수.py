def solution(array, commands):
    answer = []
    # 코멘드를 반복하면서
    for command in commands: 
        # 커멘드의 0,1 번째 만큼 자르고 
        arr = array[command[0]-1 : command[1]]
        print(sorted(arr))
        # 정렬후 3번째 항목 추출
        answer.append(sorted(arr)[command[2]-1])
    return answer
def solution(genres, plays):
    answer = []
    # 해쉬맵 만들기
    hm = {}
    sum_m = {}
    
    for i in range(len(genres)): 
        if genres[i] not in hm: 
            hm[genres[i]] = [(i, plays[i])]
            sum_m[genres[i]] = plays[i]
        else: 
            hm[genres[i]].append((i, plays[i]))
            sum_m[genres[i]] += plays[i]
    
    for key in hm.keys() : 
        hm[key].sort(key = lambda x : x[0])
        print(hm)
        hm[key].sort(key = lambda x : x[1], reverse = True)
        print(hm)
    
    sorted_keys = sorted(sum_m.items(), key = lambda x : x[1] ,reverse=True)
    print(sorted_keys)
    
    for key, i in sorted_keys:
        if len(hm[key]) == 1: 
            answer.append(hm[key][0][0])
        else: 
            answer.append(hm[key][0][0])
            answer.append(hm[key][1][0])
    
    return answer


# 필요데이터 
# 1. 장르별 총 재생횟수 
# 2. 해당 장르의 재생횟수 리스트 -> 인덱스 정보 잃으면 안됌
# 장르별 해쉬맵에 튜플로 재생횟수, 인덱스 추가?
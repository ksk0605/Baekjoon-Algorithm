def solution(today, terms, privacies):
    _today = int(today[2:4]) * 336 + int(today[5:7]) * 28 + int(today[8:10]) # 날짜를 일수로 변환
    
    _terms = {}
    for i in terms:
        _terms[i[0]] = int(i[2:]) * 28
    print(_terms)
    
    pri_dates = [] # 날짜를 일수로 변환한 정보를 담을 리스트
    pri_types = [] # 약관 종류를 담을 리스트
    
    for pri in privacies: 
        date = int(pri[2:4]) * 336 + int(pri[5:7]) * 28 + int(pri[8:10]) 
        
        pri_dates.append(date)
        pri_types.append(pri[11])

        
    answer = []
    
    for i in range(len(privacies)):
        term = _terms[pri_types[i]]
        print(term)
        limit = pri_dates[i] + term
        print(limit, _today)
        
        if limit <= _today:
            answer.append(i+1)
        
        
    return answer
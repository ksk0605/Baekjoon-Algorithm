from collections import deque 

def solution(prices):
    answer = []
    prices = deque(prices)
    
    # prices의 원소가 있을 동안에만
    while prices: 
        price = prices.popleft()
        
        cnt = 0 
        
        # 팝 한 원소를 남은 원소들과 비교하며 작거나 같을 때까지만 카운트
        for i in prices: 
            cnt += 1
            if price > i: 
                break
        answer.append(cnt)
        
    return answer
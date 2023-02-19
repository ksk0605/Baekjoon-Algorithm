from itertools import product



def solution(users, emoticons):
    discount_rates = [10,20,30,40] 
    rep = len(emoticons)
    rate_list = list(product(discount_rates, repeat = rep))

    results = []
    for rate in rate_list:
        money_sum = 0
        plus_member = 0
        for user in users:
            user_rate = user[0]
            user_limit = user[1]
            money = 0
            for i in range(rep):
                if rate[i] >= user_rate:
                    money += emoticons[i] * ((100-rate[i]) / 100)
            if money>=user_limit :
                money = 0
                plus_member += 1
            money_sum += money
        results.append([plus_member, int(money_sum)])
        
        
    results.sort(key=lambda x : (x[0], x[1]))
    print(results[-1])
    

    return results[-1]
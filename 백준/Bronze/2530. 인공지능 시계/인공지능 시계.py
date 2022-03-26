hour, minute, sec = map(int,input().split()) 
add = int(input())

total = hour * 3600 + minute * 60 + sec + add # 전체 총 시간을 초단위로 합산
hour = (total // 3600)%24 # 시간 계산 24시간부터는 0시간부터 다시 시작
total -= (total//3600) * 3600
minute = total // 60
total -= (total // 60) * 60
sec = total

print(hour,minute,sec)
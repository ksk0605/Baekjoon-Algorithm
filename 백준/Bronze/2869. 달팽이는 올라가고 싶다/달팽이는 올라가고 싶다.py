import math

a,b,v = map(int, input().split())

k = a-b
count = math.ceil(((v-a)/k)) + 1 # 올림 함수를 이용하여 .x일을 하루로 계산해줌

print(count)
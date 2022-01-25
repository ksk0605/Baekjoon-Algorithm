n = int(input())

scores = list(map(int,input().split()))

scores.sort()

max = scores[-1]
sum = 0

for i in scores:
  sum += i/max*100

print(sum/n)
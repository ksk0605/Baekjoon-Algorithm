n = int(input())

for _ in range(n):
  line = list(map(int,input().split()))
  ever = sum(line[1:])/line[0]
  count = 0
  for i in line[1:]:
    if i > ever:
      count += 1
  per = (count/line[0]) * 100
  print(f'{per:.3f}%')
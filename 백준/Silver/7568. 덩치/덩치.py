n = int(input())
people = [] # 선수 리스트
rank = [0 for _ in range(n)] # 랭크 리스트

for _ in range(n):
  people.append(list(map(int, input().split())))

r = 1 # 기본등수는 1
for i in range(n):
  for j in range(n):
    if (people[i][0] < people[j][0]) and (people[i][1] < people[j][1]): #나보다 큰 사람이 있으면 등수 up
      r += 1
  rank[i] = r
  r = 1

for i in range(n):
  print(rank[i], end='')
  print(' ',end='')
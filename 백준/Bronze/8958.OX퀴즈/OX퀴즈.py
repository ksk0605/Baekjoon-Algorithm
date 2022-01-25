n = int(input())

for _ in range(n):
  quiz = input()
  count = 0 
  score = 0
  for j in quiz:
    if j == 'O':
      count += 1
      score += count
    else:
      count = 0
  print(score) 
n = int(input())

movie = 666
i = 0
while True:
  s = list(str(movie))
  cnt = 0
  for k in reversed(s):
    if k == '6':
      cnt += 1
    else:
      cnt = 0
    if cnt == 3:
      break
  if cnt == 3:
    i+=1
  if i == n:
    break
  else:
    movie+=1 
print(movie)
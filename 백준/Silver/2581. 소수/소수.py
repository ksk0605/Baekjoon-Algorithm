m = int(input())
n = int(input())

test = 2
t = True

s = []

for i in range(m,n+1):
  if i == 1:
    continue
  if i == 2:
    s.append(i)
    continue
  while test < i:
    if i%test == 0:
      t = False
      break
    test += 1
  if t == True:
    s.append(i)  
  test = 2
  t = True

if len(s) == 0:
  print(-1)
else:
  print(sum(s))
  print(s[0])
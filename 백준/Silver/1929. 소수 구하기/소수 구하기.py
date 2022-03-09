import math

n, m = map(int, input().split())

for i in range(n,m+1):

  if i == 1:
    continue
  elif i == 2:
    print(i)
    continue
  else:
    k = 2
    t = True  
    while k<=math.sqrt(i):
      if i%k == 0:
        t = False
        break
      k+=1
    if t == True:
      print(i)
n = int(input())

count = 0
temp = 1

while n > 0:
  n -= temp
  temp += 1
  count += 1
if count%2 == 1:
  print(str(1-n)+ '/' + str(n+count))
else:
  print(str(n+count)+'/'+str(1-n))  

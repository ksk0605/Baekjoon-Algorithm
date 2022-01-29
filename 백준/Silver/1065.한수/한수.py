n = int(input())

if n<=99:
  print(n)
else:
  numlist = list(range(100,n+1))
  count = 0
  for i in numlist:
    num = list(map(int, str(i)))
    if (num[1]-num[0]) == (num[2]-num[1]):
      count += 1
  print(99+count)
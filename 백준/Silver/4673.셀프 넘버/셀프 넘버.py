numlist = list(range(1,10001))
list2 = list(range(1, 10000))
for i in numlist:
  num = list(map(int, str(i)))
  snum = sum(num) + i
  if snum in list2:
    list2.remove(snum)
for i in list2:
  print(i)
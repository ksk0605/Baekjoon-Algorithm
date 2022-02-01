s = input().upper()

alfaset = list(set(s))
sizelist = []

for i in alfaset:
  sizelist.append(s.count(i))

if sizelist.count(max(sizelist)) >= 2:
  print('?')
else:
  ind = sizelist.index(max(sizelist))
  print(alfaset[ind])

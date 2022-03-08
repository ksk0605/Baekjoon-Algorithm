n = int(input())

test = 2
t = True

count = 0

l = list(map(int, input().split()))
for i in l:
  if i == 1:
    continue
  if i == 2:
    count += 1
    continue
    
  while test<i:
    if i%test == 0:
      t = False
      break
    test += 1
  if t == True:
    count += 1
  test = 2
  t = True

print(count)
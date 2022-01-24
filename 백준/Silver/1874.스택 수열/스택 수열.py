n = int(input())

count = 1
stack = []
result = []
can = True

for _ in range(n):
  num = int(input())
  
  while count <= num:
    stack.append(count)
    count += 1
    result.append('+')
  
  if stack[-1] == num:
    result.append('-')
    stack.pop()
  else:
    can = False
    break

if can == True:
  for i in result:
    print(i)
else:
  print("NO")

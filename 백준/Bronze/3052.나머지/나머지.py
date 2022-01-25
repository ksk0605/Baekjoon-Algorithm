stack = [] 
for _ in range(10): 
  n = int(input())

  if  n%42 in stack:
    continue
  else:
    stack.append(n%42)

print(len(stack))
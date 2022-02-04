n = int(input())

stack = [] 

for _ in range(n):
  s = int(input())
  stack.append(s)
stack.sort()

for i in stack:
  print(i) 
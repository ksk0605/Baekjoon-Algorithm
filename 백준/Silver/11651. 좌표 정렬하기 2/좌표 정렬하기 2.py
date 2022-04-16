n = int(input())

l = []
for _ in range(n):
  l.append(list(map(int, input().split()))) 

l.sort(key = lambda x:x[0])
l.sort(key = lambda x:x[1])

for i in l:
  print(i[0], i[1])
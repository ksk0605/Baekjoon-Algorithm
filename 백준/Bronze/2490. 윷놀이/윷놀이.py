import sys
input = sys.stdin.readline

for i in range(3):
  res = list(map(int, input().split()))
  s = sum(res)
  if s == 1:
    print('C')
  elif s == 2:
    print('B')
  elif s == 3:
    print('A')
  elif s == 0:
    print('D')
  else:
    print('E')
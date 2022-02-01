n = int(input())

for n in range(n):
  k, s = input().split()
  new = []
  for i in s:
    for _ in range(int(k)):
      new.append(i)
  print("".join(map(str, new)))
import sys
input = sys.stdin.readline

s = []
for _ in range(9):
  s.append(int(input()))

s.sort()
k = sum(s)

for i in range(9):
  for j in range(i+1, 9):
    outn = s[i]
    inn = s[j]
    if (k - outn - inn) == 100:
      s.remove(outn)
      s.remove(inn)
      break
  if len(s) == 7:
    break


for i in s:
  print(i)
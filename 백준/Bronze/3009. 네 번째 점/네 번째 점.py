s1 = []
s2 = []
for _ in range(3):
  a,b = map(int, input().split())
  if a in s1:
    s1.remove(a)
  else:
    s1.append(a)
  if b in s2:
    s2.remove(b)
  else:
    s2.append(b)

print(s1[0], s2[0])
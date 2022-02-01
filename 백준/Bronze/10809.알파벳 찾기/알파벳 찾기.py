s = input()

for i in range(97,123):
  if chr(i) in s:
    print(s.index(chr(i)))
  else:
    print(-1)
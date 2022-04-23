n, m = map(int,input().split())

cards = list(map(int, input().split()))

M = 0

for i in range(n):
  for j in range(i+1, n):
    for k in range(j+1, n):
      temp = cards[i]+cards[j]+cards[k]
      if m == temp:
        M = m
        break
      elif temp < m and temp>M:
        M = temp

print(M)
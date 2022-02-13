k = int(input())

s = []
for _ in range(k):
  n = list(map(int, input().split()))
  s.append(n)

s.sort() # 정렬

for i in s:
  k = ' '.join(str(j) for j in i) # 문자열로 변환
  print(k)
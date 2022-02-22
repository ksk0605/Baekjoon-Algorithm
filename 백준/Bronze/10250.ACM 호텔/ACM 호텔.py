n = int(input())

for _ in range(n):
  h, w, m = map(int, input().split())
  num = m//h + 1
  floor = m%h
  if m%h == 0: # 손님 숫자가 층의 배수일때
    floor = h
    num = m//h
  if len(str(num)) == 1:
    num = str(num).zfill(2)
  else:
    num = str(num)
  print(str(floor)+num)
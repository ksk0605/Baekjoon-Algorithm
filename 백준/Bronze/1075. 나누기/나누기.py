n = int(input())
m = int(input())

n = n-n%100
num = n
while True:
  if n%m == 0:
    num = n%100
    break;
  n += 1
num = str(num)
print(num.zfill(2))
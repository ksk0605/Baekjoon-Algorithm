n = int(input())

check =False

for i in range(1, n+1):
  l = list(map(int, str(i)))

  divSum = i + sum(l)
  if divSum == n:
    print(i)
    check =True
    break;

if check == False:
  print(0)
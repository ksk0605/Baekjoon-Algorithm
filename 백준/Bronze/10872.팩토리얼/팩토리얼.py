def facto(n):
  result = 1
  if n == 0:
    return 1
  else:
    for i in range(1,n+1):
      result *= i
    return result

n = int(input())

print(facto(n))
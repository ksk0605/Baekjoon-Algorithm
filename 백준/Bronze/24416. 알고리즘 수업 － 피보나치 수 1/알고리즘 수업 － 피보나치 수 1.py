def fibonacci(n):
  global num2
  
  f = [0]*50
  f[1] = f[2] = 1
  for i in range(3,n+1):
    f[i] = f[i - 1] + f[i - 2]  # 코드2
  return f[n]


n = int(input())
print(fibonacci(n), n-2)
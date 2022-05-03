n = int(input())

i = 1
sum = 0
while sum<n:
  sum += i
  i += 1

sum -= i-1
print(max(i-2, n-sum))
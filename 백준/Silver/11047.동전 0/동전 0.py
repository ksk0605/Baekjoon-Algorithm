n, m = map(int, input().split())
stack = []
for _ in range(n):
  coin = int(input())
  stack.append(coin)

count = 0
for i in reversed(stack):
  if m//i > 0:
    count += m//i
    m = m%i

print(count)
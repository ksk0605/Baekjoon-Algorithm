n = int(input())
l = list(map(int, input().split()))

l.sort()

s= 0
for i in range(n):
  s += sum(l[:i])
  s += l[i]

print(s)
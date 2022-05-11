n = int(input())
l= list(map(int, input().split()))
n = int(input())

cnt = 0
for i in l:
  if i == n:
    cnt+=1

print(cnt)    
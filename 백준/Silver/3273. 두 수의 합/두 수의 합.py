n = int(input())
l= list(map(int, input().split()))
n = int(input())

nlist = [0] *  2000004

for i in l:
  nlist[n-i] += 1

cnt = 0
for i in l:
  cnt += nlist[i]

print(cnt // 2)
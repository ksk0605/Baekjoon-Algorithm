def binsearch(l, left, right, key): # 이분탐색 알고리즘
  m = (left + right)//2
  if left > right:
    return -1
  if l[m] == key:
    return m
  elif l[m] < key:
    return binsearch(l, m+1, right, key)
  elif l[m] > key:
    return binsearch(l, left, m-1,key)


n = int(input())

l = list(map(int, input().split()))
l.sort() #정렬

n = int(input())
s = list(map(int, input().split()))

for i in s: #원소가 있는지 하나씩 검사
  if binsearch(l,0,len(l)-1, i) == -1: # -1 반환시 찾지 못한 경우
    print(0)
  else:
    print(1)
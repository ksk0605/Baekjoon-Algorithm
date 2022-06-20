n = int(input())
card = set(map(int, input().split()))

n = int(input())
nums = list(map(int, input().split()))

for i in nums:
  if i in card:
    print('1 ', end='')
  else:
    print('0 ', end='')
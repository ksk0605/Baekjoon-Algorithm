cost = int(input())
n = int(input())
for i in range(n):
    price, k = map(int, input().split())
    cost -= k*price

if cost == 0:
    print('Yes')
else:
    print('No')
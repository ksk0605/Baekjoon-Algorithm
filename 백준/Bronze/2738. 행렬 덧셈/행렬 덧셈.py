n,m = map(int, input().split())
a = []
b = [] 
for i in range(2*n):
    if i<n:
        a.append(list(map(int, input().split())))
    else:
        b.append(list(map(int, input().split())))


for i in range(n):
    for j in range(m):
        a[i][j] += b[i][j]
        print(a[i][j], end=' ')
    print()
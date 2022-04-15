n = int(input())

meet = []
for _ in range(n):
    meet.append(list(map(int, input().split())))

meet.sort(key = lambda x:x[0])
meet.sort(key = lambda x:x[1])

end = 0
cnt = 0 

for i,j in meet:
    if i>=end:
        cnt += 1
        end = j

print(cnt)
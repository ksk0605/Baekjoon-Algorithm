x,y,w,h = map(int, input().split())

mnum = min(x,y)

mnum = min(mnum,min((w-x),(h-y)))

print(mnum)
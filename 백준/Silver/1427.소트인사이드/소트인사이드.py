s = list(map(int,input()))
s.sort(reverse=True)
a = ''.join(map(str, s))
print(a)
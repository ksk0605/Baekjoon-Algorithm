n, k = map(int, input().split())

l = list(range(1, n+1))

current = k-1

s = []
while True:
    s.append(l.pop(current))
    if len(l) == 0:
        break
    current = (current + (k-1)) % len(l)

s = str(s)[1:-1]
print('<'+s+'>')
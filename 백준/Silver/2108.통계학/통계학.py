import sys
from collections import Counter
n = int(sys.stdin.readline())

s = []
for _ in range(n):
  s.append(int(sys.stdin.readline()))

s.sort()

print(round(sum(s)/n))

print(s[n//2])

cnt_s = Counter(s).most_common()
if len(cnt_s) > 1 and cnt_s[0][1]==cnt_s[1][1]: #최빈값 2개 이상
    print(cnt_s[1][0])
else:
    print(cnt_s[0][0])

print(s[-1] - s[0])
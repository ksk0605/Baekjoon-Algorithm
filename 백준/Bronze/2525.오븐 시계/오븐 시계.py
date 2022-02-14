hour, minute = map(int, input().split())
add = int(input())

n = minute + add
if n > 59:
  hour += n//60
  minute = n%60
else:
  minute = n
if hour>23:
  hour %= 24

print(hour,minute) 
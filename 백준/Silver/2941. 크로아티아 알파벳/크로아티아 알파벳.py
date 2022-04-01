check = ['=', '-', 'j']

s = input()

size = len(s)

for i in range(size):
  if s[i] in check:
    if s[i] == '=':
      if s[i-1] == 'z':
        if s[i-2] == 'd':
          size -= 2
        else:
          size -= 1
      else:
        size -= 1
    elif s[i] == '-':
      size -= 1
    elif s[i] == 'j':
      if (s[i-1] == 'l') or (s[i-1] == 'n'):
        size -= 1
print(size)
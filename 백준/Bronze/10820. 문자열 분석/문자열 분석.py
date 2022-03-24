import sys

while True:
    s = sys.stdin.readline().rstrip('\n')
    analy = [0, 0, 0 ,0]
    if not s:
        break
    for i in s:
        if i.isdigit():
            analy[2] += 1
        if i.isalpha():
            if 65 <= ord(i) <= 90:
                analy[1]+=1
            elif 97 <= ord(i) <= 122:
                analy[0]+=1
        if i == ' ':
            analy[3] += 1
    print(analy[0], analy[1], analy[2], analy[3])
n = int(input())
kinds = map(int, input().split())

result = 0
for chicken in kinds:
    difference = chicken - n
    if difference >= 0:
        result += n
    else: 
        result += chicken

print(result)

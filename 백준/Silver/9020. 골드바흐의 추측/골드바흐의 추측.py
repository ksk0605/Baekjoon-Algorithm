def isPrime(n) :
    if n == 1:
        return False
    if n == 2:
        return True
    
    bound = n**0.5
    i = 2
    while i<=bound:
        if n%i == 0:
            return False
        i+=1

    return True

n = int(input())

for i in range(n):
    num = int(input())
    right = num // 2
    left = num - right
    while left > 0 :
        if (isPrime(left) and isPrime(right)):
            print(left, right)
            break
        left -= 1
        right = num - left
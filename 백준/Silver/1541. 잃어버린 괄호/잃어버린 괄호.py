formula = list(input())
num = []
s = []


for i in range(len(formula)):
  if formula[i] == '-' or formula[i] == '+':
    num = int("".join(num))
    s.append(num)
    s.append(formula[i])
    num = []
    continue
    
  num.append(formula[i])
  
  if i == len(formula) - 1:
    num = int("".join(num))
    s.append(num)


plus = 0
minus = 0
tcheck = True

for i in s:
  if i == '-':
    tcheck = False
    
  if isinstance(i, int) and tcheck == True:
    plus += i
  elif isinstance(i, int) and tcheck == False:
    minus += i
  
  
print(plus-minus)
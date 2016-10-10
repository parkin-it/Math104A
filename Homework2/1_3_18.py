#Solution to problem 1.3: 18

import math

error = 1
i = 1
while error >= 10**(-2):
    for n in range(1,i+1):
        sum = sum + 1/n
        
    sum = sum +1/n - math.log(n)
    i = i+1
    error = abs(.5772156649-sum)
    sum = 0

print(n)
print(error)

while error >= 10**(-3):
    for n in range(1,i+1):
        sum = sum + 1/n
        
    sum = sum +1/n - math.log(n)
    i = i+1
    error = abs(.5772156649-sum)
    sum = 0

print(n)
print(error)

while error >= 10**(-4):
    for n in range(1,i+1):
        sum = sum + 1/n
        
    sum = sum +1/n - math.log(n)
    i = i+1
    error = abs(.5772156649-sum)
    sum = 0

print(n)
print(error)
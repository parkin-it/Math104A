#Solution to problem 1.3: 2bcd

import sys
sys.path.insert(0, '/Users/oracle/Python/K_Digit/')

import k_digit

#2b
b = 0

for j in range(5,0,-1):
    tmp = k_digit.divide(1,k_digit.factorial(j,4,"chop"),4,"chop")
    b = k_digit.add(tmp,b,4,"chop")

b = k_digit.add(b,1,4,"chop")
   
print("Answer for 2b: " + str(b))

#2c
c = 0

for i in range(1,10):
    tmp = k_digit.divide(1,k_digit.factorial(i,4,"chop"),4,"chop")
    c = k_digit.add(tmp,c,4,"chop")

c = k_digit.add(c,1,4,"chop")

print("Answer for 2c: " + str(c))

#2d
d = 0

for j in range(10,0,-1):
    tmp = k_digit.divide(1,k_digit.factorial(j,4,"chop"),4,"chop")
    d = k_digit.add(tmp,d,4,"chop")

d = k_digit.add(d,1,4,"chop")
   
print("Answer for 2d: " + str(d))
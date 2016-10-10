#Solution to problem 1.3: 1

import sys
sys.path.insert(0, '/Users/oracle/Python/K_Digit/')

import k_digit

sum = 0
sum_forward = 0
sum_reverse = 0

# Sum using floating point numbers
for i in range(1,10):
    sum = 1/i**2+sum

#Sum using k-digit chopping in the forward direction
for i in range(1,10):
    sum_forward = k_digit.add(1/i**2,sum_forward,3,"chop")
    
#Sum using k-digit chopping in the reverse direction
for i in range(10,0, -1):
    sum_reverse = k_digit.add(1/i**2,sum_reverse,3,"chop")

print("Sum no chopping: "+str(sum))
print("Sum Forward: "+str(sum_forward))
print("Sum Reverse: "+str(sum_reverse))
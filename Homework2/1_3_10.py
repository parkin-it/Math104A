#Solution to problem 1.3: 10
import math

a = 1
b = 10
c = -4

#Use the equation and catch imaginary results
try:
    xa = (-2*c)/(b+math.sqrt(b**2-4*a*c))
except ValueError:
    xa = float('nan')

try:
    xb = (-b-math.sqrt(b**2-4*a*c))/(2*a)
except ValueError:
    xb = float('nan')
    
print(xa)
print(xb)
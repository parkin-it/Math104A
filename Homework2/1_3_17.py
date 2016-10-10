#Solution to problem 1.3: 17                                                                                                                                                          
import math

n = 100

Fsub_n=(1/math.sqrt(5))*((((1+math.sqrt(5))/2)**n)-(((1-math.sqrt(5))/2)**n))

print("Fn = " + str(Fsub_n))
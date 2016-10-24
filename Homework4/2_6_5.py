#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 16:44:36 2016

@author: Nathan A Cheadle
"""

import sys
sys.path.insert(0, '/Users/oracle/Python/Math104A/SolutionOneVariable/')

import OneVariableSolution as OVS
import numpy as np
import matplotlib.pyplot as plt

print("--------------A---------------")
equation = "x**3-9*x**2+12"
derivative = "3*x**2-18*x"

guess = -1
p_out = OVS.newton(guess,equation,derivative,10e-4)
print("Final result for guess = " +str(guess)+ " of equation: " + equation+ " = " + str(p_out))

guess = 3
p_out = OVS.newton(guess,equation,derivative,10e-4)
print("Final result for guess = " +str(guess)+ " of equation: " + equation+ " = " + str(p_out))

guess = 8
p_out = OVS.newton(guess,equation,derivative,10e-4)
print("Final result for guess = " +str(guess)+ " of equation: " + equation+ " = " + str(p_out))

x = np.arange(-2, 10, 0.01)
y = eval(equation)
plt.plot(x, y)
plt.title('Homework 4 Problem 2.6 - 5a')
plt.grid(True)
plt.savefig("2_6_5a.png")
plt.show()

print("--------------A---------------")
equation = "x**4-2*x**3-5*x**2+12*x-5"
derivative = "4*x**3-6*x**2-10*x+12"

x = np.arange(-2, 2, 0.01)
y = eval(derivative)
plt.plot(x, y)
plt.title('Homework 4 Problem 2.6 - 5b - derivative of f(x)')
plt.grid(True)
plt.savefig("2_6_5b.png")
plt.show()

guess = -2
p_out = OVS.newton(guess,equation,derivative,10e-4)
print("Final result for guess = " +str(guess)+ " of equation: " + equation+ " = " + str(p_out))

guess = 0
p_out = OVS.newton(guess,equation,derivative,10e-4)
print("Final result for guess = " +str(guess)+ " of equation: " + equation+ " = " + str(p_out))

guess = 1.5
p_out = OVS.newton(guess,equation,derivative,10e-4)
print("Final result for guess = " +str(guess)+ " of equation: " + equation+ " = " + str(p_out))

guess = 3
p_out = OVS.newton(guess,equation,derivative,10e-4)
print("Final result for guess = " +str(guess)+ " of equation: " + equation+ " = " + str(p_out))

print("f(-1.5) = " + str(OVS.f_x(equation, -1.5)))
print("f(1) = " + str(OVS.f_x(equation, 1)))
print("f(2) = " + str(OVS.f_x(equation, 2)))
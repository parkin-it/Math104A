#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 16:00:48 2016

@author: Nathan A Cheadle
"""

import sys
sys.path.insert(0, '/Users/oracle/Python/Math104A/SolutionOneVariable/')

import OneVariableSolution as OVS
import numpy as np
import matplotlib.pyplot as plt

print("--------------A---------------")
equation = "x**3-2*x**2-5"
derivative = "3*x**2-4*x"

x = np.arange(0, 3, 0.01)
y = eval(equation)
plt.plot(x, y)
plt.title('Homework 4 Problem 2.6 - 1a')
plt.grid(True)
plt.savefig("2_6_1a.png")
plt.show()

guess = 2.5
p_out = OVS.newton(guess,equation,derivative,10e-4)
print("Final result for guess = " +str(guess)+ " of equation: " + equation+ " = " + str(p_out))

print("--------------B---------------")
equation = "x**3+3*x**2-1"
derivative = "3*x**2+6*x"

x = np.arange(-4, 2, 0.01)
y = eval(equation)
plt.plot(x, y)
plt.title('Homework 4 Problem 2.6 - 1b')
plt.grid(True)
plt.savefig("2_6_1b.png")
plt.show()

guess = 0.5
p_out = OVS.newton(guess,equation,derivative,10e-4)
print("Final result for guess = " +str(guess)+ " of equation: " + equation+ " = " + str(p_out))

guess = -.5
p_out = OVS.newton(guess,equation,derivative,10e-4)
print("Final result for guess = " +str(guess)+ " of equation: " + equation+ " = " + str(p_out))

guess = -3
p_out = OVS.newton(guess,equation,derivative,10e-4)
print("Final result for guess = " +str(guess)+ " of equation: " + equation+ " = " + str(p_out))

print("--------------C---------------")
equation = "x**3-x-1"
derivative = "3*x**2-1"

x = np.arange(-2, 2, 0.01)
y = eval(equation)
plt.plot(x, y)
plt.title('Homework 4 Problem 2.6 - 1c')
plt.grid(True)
plt.savefig("2_6_1c.png")
plt.show()

guess = 1.25
p_out = OVS.newton(guess,equation,derivative,10e-4)
print("Final result for guess = " +str(guess)+ " of equation: " + equation+ " = " + str(p_out))

print("--------------D---------------")
equation = "x**4+2*x**2-x-3"
derivative = "4*x**3+4*x-1"

x = np.arange(-2, 2, 0.01)
y = eval(equation)
plt.plot(x, y)
plt.title('Homework 4 Problem 2.6 - 1d')
plt.grid(True)
plt.savefig("2_6_1d.png")
plt.show()

guess = -1
p_out = OVS.newton(guess,equation,derivative,10e-4)
print("Final result for guess = " +str(guess)+ " of equation: " + equation+ " = " + str(p_out))

guess = 1
p_out = OVS.newton(guess,equation,derivative,10e-4)
print("Final result for guess = " +str(guess)+ " of equation: " + equation+ " = " + str(p_out))

print("--------------E---------------")
equation = "x**3+4.001*x**2+4.002*x+1.101"
derivative = "3*x**2+8.002*x+4.002"

x = np.arange(-3, 2, 0.01)
y = eval(equation)
plt.plot(x, y)
plt.title('Homework 4 Problem 2.6 - 1e')
plt.grid(True)
plt.savefig("2_6_1e.png")
plt.show()

guess = -3
p_out = OVS.newton(guess,equation,derivative,10e-4)
print("Final result for guess = " +str(guess)+ " of equation: " + equation+ " = " + str(p_out))

guess = -1
p_out = OVS.newton(guess,equation,derivative,10e-4)
print("Final result for guess = " +str(guess)+ " of equation: " + equation+ " = " + str(p_out))

guess = 0
p_out = OVS.newton(guess,equation,derivative,10e-4)
print("Final result for guess = " +str(guess)+ " of equation: " + equation+ " = " + str(p_out))

print("--------------E---------------")
equation = "x**5-x**4+2*x**3-3*x**2+x-4"
derivative = "5*x**4-4*x**3+6*x**2-6*x+1"

x = np.arange(-1, 2, 0.01)
y = eval(equation)
plt.plot(x, y)
plt.title('Homework 4 Problem 2.6 - 1f')
plt.grid(True)
plt.savefig("2_6_1f.png")
plt.show()

guess = 1.5
p_out = OVS.newton(guess,equation,derivative,10e-4)
print("Final result for guess = " +str(guess)+ " of equation: " + equation+ " = " + str(p_out))
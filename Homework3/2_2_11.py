#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 19:04:24 2016

@author: Nathan A Cheadle
"""
import sys
sys.path.insert(0, '/Users/oracle/Python/Math104A/SolutionOneVariable/')

import OneVariableSolution as OVS
import matplotlib.pyplot as plt
import numpy as np

expression = "2/3-np.exp(x)/3+x**2/2"
error = 10e-5

p_out = OVS.fixedpoint(0, expression, error)
print("Final Guess = " + str(p_out))


x = np.arange(-3, 3, 0.01)
y = eval(expression)
plt.plot(x, y)

plt.title('Homework 3 Problem 2.2 - 11a - g(x)')
plt.grid(True)
plt.savefig("2_2_11a1.png")
plt.show()

x = np.arange(-3, 3, 0.01)
y = -1*np.exp(x)/3 +2*x/3
plt.plot(x, y)

plt.title('Homework 3 Problem 2.2 - 11a - g(x)prime')
plt.grid(True)
plt.savefig("2_2_11a2.png")
plt.show()

expression = "5/x**2+2"
error = 10e-5

p_out = OVS.fixedpoint(3, expression, error)
print("Final Guess = " + str(p_out))

x = np.arange(1.5, 5, 0.01)
y = eval(expression)
plt.plot(x, y)

plt.title('Homework 3 Problem 2.2 - 11b - g(x)')
plt.grid(True)
plt.savefig("2_2_11b1.png")
plt.show()

x = np.arange(1.5, 5, 0.01)
y = (-10)/(x**3)
plt.plot(x, y)

plt.title('Homework 3 Problem 2.2 - 11b - g(x)prime')
plt.grid(True)
plt.savefig("2_2_11b2.png")
plt.show()

expression = "(np.exp(x)/3)**.5"
error = 10e-5

p_out = OVS.fixedpoint(1, expression, error)
print("Final Guess = " + str(p_out))

x = np.arange(0, 3, 0.01)
y = eval(expression)
plt.plot(x, y)

plt.title('Homework 3 Problem 2.2 - 11c - g(x)')
plt.grid(True)
plt.savefig("2_2_11c1.png")
plt.show()

x = np.arange(0, 3, 0.01)
y = np.exp(x)/6*(np.exp(x)/3)**(-1/2)
plt.plot(x, y)

plt.title('Homework 3 Problem 2.2 - 11c - g(x)prime')
plt.grid(True)
plt.savefig("2_2_11c2.png")
plt.show()

expression = "5**-x"
error = 10e-5

p_out = OVS.fixedpoint(.5, expression, error)
print("Final Guess = " + str(p_out))

x = np.arange(0, 2, 0.01)
y = eval(expression)
plt.plot(x, y)

plt.title('Homework 3 Problem 2.2 - 11d - g(x)')
plt.grid(True)
plt.savefig("2_2_11d1.png")
plt.show()

x = np.arange(0, 2, 0.01)
y = -5**(-x)*np.log(5)
plt.plot(x, y)

plt.title('Homework 3 Problem 2.2 - 11d - g(x)prime')
plt.grid(True)
plt.savefig("2_2_11d2.png")
plt.show()

expression = "6**-x"
error = 10e-5

p_out = OVS.fixedpoint(.5, expression, error)
print("Final Guess = " + str(p_out))

x = np.arange(0, 2, 0.01)
y = eval(expression)
plt.plot(x, y)

plt.title('Homework 3 Problem 2.2 - 11e - g(x)')
plt.grid(True)
plt.savefig("2_2_11e1.png")
plt.show()

x = np.arange(0, 2, 0.01)
y = -6**(-x)*np.log(6)
plt.plot(x, y)

plt.title('Homework 3 Problem 2.2 - 11e - g(x)prime')
plt.grid(True)
plt.savefig("2_2_11e2.png")
plt.show()

expression = ".5*(np.sin(x)+np.cos(x))"
error = 10e-5

p_out = OVS.fixedpoint(0, expression, error)
print("Final Guess = " + str(p_out))

x = np.arange(0, np.pi, 0.01)
y = eval(expression)
plt.plot(x, y)

plt.title('Homework 3 Problem 2.2 - 11f - g(x)')
plt.grid(True)
plt.savefig("2_2_11f1.png")
plt.show()

x = np.arange(0, np.pi, 0.01)
y = .5*(np.cos(x)-np.sin(x))
plt.plot(x, y)

plt.title('Homework 3 Problem 2.2 - 11f - g(x)prime')
plt.grid(True)
plt.savefig("2_2_11f2.png")
plt.show()
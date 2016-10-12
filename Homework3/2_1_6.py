#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 14:47:29 2016

@author: Nathan A Cheadle
"""

import sys
sys.path.insert(0, '/Users/oracle/Python/Math104A/SolutionOneVariable/')

import OneVariableSolution as OVS
import matplotlib.pyplot as plt
import numpy as np

print("-------------------A---------------------")

expression = "3*x-np.exp(x)"
error = 10e-5
p_out = OVS.bisection(1,2,expression,error)
print("Final Guess = " + str(p_out))

x = np.arange(1, 2, 0.01)
y = eval(expression)
plt.plot(x, y)

plt.title('Homework 3 Problem 2.1 - 6a')
plt.grid(True)
plt.savefig("2_1_6a.png")
plt.show()

print("-------------------B---------------------")

expression = "2*x+3*np.cos(x)-np.exp(x)"
error = 10e-5
p_out = OVS.bisection(1,2,expression,error)
print("Final Guess = " + str(p_out))

x = np.arange(1,2, 0.01)
y = eval(expression)
plt.plot(x, y)

plt.title('Homework 3 Problem 2.1 - 6b')
plt.grid(True)
plt.savefig("2_1_6b.png")
plt.show()

print("-------------------C---------------------")

expression = "x**2-4*x+4-np.log(x)"
error = 10e-5
p_out = OVS.bisection(1,2,expression,error)
print("Final Guess = " + str(p_out))
p_out = OVS.bisection(2,4,expression,error)
print("Final Guess = " + str(p_out))

x = np.arange(1,4, 0.01)
y = eval(expression)
plt.plot(x, y)

plt.title('Homework 3 Problem 2.1 - 6c')
plt.grid(True)
plt.savefig("2_1_6c.png")
plt.show()

print("-------------------D---------------------")

expression = "x+1-2*np.sin(np.pi*x)"
error = 10e-5
p_out = OVS.bisection(0, .5,expression,error)
print("Final Guess = " + str(p_out))
p_out = OVS.bisection(.5, 1,expression,error)
print("Final Guess = " + str(p_out))

x = np.arange(0,1, 0.01)
y = eval(expression)
plt.plot(x, y)

plt.title('Homework 3 Problem 2.1 - 6d')
plt.grid(True)
plt.savefig("2_1_6d.png")
plt.show()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 15:21:30 2016

@author: Nathan A Cheadle
"""

import sys
sys.path.insert(0, '/Users/oracle/Python/Math104A/SolutionOneVariable/')

import OneVariableSolution as OVS
import matplotlib.pyplot as plt
import numpy as np

expression = "(x+2)*(x+1)*x*(x-1)**3*(x-2)"
error = 10e-3

print("-------------------A---------------------")
p_out = OVS.bisection(-3, 2.5,expression,error)
print("Final Guess = " + str(p_out))

print("-------------------B---------------------")
p_out = OVS.bisection(-2.5,3,expression,error)
print("Final Guess = " + str(p_out))

print("-------------------C---------------------")
p_out = OVS.bisection(-1.75,1.5,expression,error)
print("Final Guess = " + str(p_out))

print("-------------------D---------------------")
p_out = OVS.bisection(-1.5,1.75,expression,error)
print("Final Guess = " + str(p_out))

x = np.arange(-2, 2, 0.01)
y = eval(expression)
plt.plot(x, y)

plt.title('Homework 3 Problem 2.1 - 11')
plt.grid(True)
plt.savefig("2_1_11.png")
plt.show()
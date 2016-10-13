#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 14:32:31 2016

@author: Nathan A Cheadle
"""

import sys
sys.path.insert(0, '/Users/oracle/Python/Math104A/SolutionOneVariable/')

import OneVariableSolution as OVS
import matplotlib.pyplot as plt
import numpy as np

expression = "x**4-2*x**3-4*x**2+4*x+4"
error = 10e-2

p_out = OVS.bisection(-2,-1,expression,error)
print("Final Guess = " + str(p_out))

p_out = OVS.bisection(0,2,expression,error)
print("Final Guess = " + str(p_out))

p_out = OVS.bisection(2,3,expression,error)
print("Final Guess = " + str(p_out))

p_out = OVS.bisection(-1,0,expression,error)
print("Final Guess = " + str(p_out))

x = np.arange(-2, 3, 0.01)
y = eval(expression)
plt.plot(x, y)

plt.title('Homework 3 Problem 2.1 - 4')
plt.grid(True)
plt.savefig("2_1_4.png")
plt.show()
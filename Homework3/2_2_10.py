#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 18:54:50 2016

@author: Nathan A Cheadle
"""

import sys
sys.path.insert(0, '/Users/oracle/Python/Math104A/SolutionOneVariable/')

import OneVariableSolution as OVS
import matplotlib.pyplot as plt
import numpy as np

expression = "x**3-25"
error = 10e-4

p_out = OVS.bisection(0,3,expression,error)
print("Final Guess = " + str(p_out))

x = np.arange(0, 3, 0.01)
y = eval(expression)
plt.plot(x, y)

plt.title('Homework 3 Problem 2.2 - 10')
plt.grid(True)
plt.savefig("2_1_10.png")
plt.show()

expression = "x-(x**3-25)/(3*x**2)"
error = 10e-4

p_out = OVS.fixedpoint(1.5, expression, error)
print("Final Guess = " + str(p_out))
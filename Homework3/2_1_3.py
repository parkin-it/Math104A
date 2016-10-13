#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 17:48:43 2016

@author: Nathan A Cheadle
"""

import sys
sys.path.insert(0, '/Users/oracle/Python/Math104A/SolutionOneVariable/')

import OneVariableSolution as OVS
import matplotlib.pyplot as plt
import numpy as np

expression = "x**3-7*x**2+14*x-6"
error = 10e-2

p_out = OVS.bisection(0,1,expression,error)
print("Final Guess = " + str(p_out))

p_out = OVS.bisection(1,3.2,expression,error)
print("Final Guess = " + str(p_out))

p_out = OVS.bisection(3.2,4,expression,error)
print("Final Guess = " + str(p_out))

x = np.arange(0.0, 4, 0.01)
y = eval(expression)
plt.plot(x, y)

plt.title('Homework 3 Problem 2.1 - 3')
plt.grid(True)
plt.savefig("2_1_3.png")
plt.show()
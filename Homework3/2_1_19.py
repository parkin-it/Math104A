#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 16:28:34 2016

@author: Nathan A Cheadle
"""

import sys
sys.path.insert(0, '/Users/oracle/Python/Math104A/SolutionOneVariable/')

import OneVariableSolution as OVS
import matplotlib.pyplot as plt
import numpy as np

expression = "10*np.sqrt(0.5*np.pi*1**2-1**2*np.arcsin(x/1)-x*(1**2-x**2))-12.3"
error = 1e-2

p_out = OVS.bisection(0,1,expression,error)
print("Final Guess = " + str(p_out))

x = p_out
V = 10*np.sqrt(0.5*np.pi*1**2-1**2*np.arcsin(x/1)-x*(1**2-x**2))
print("Volume based on Height Input = "+str(V))

x = np.arange(0, 1, 0.01)
y = eval(expression)
plt.plot(x, y)

plt.title('Homework 3 Problem 2.1 - 19')
plt.grid(True)
plt.savefig("2_1_19.png")
plt.show()
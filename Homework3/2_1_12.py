#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 15:32:05 2016

@author: Nathan A Cheadle
"""

import sys
sys.path.insert(0, '/Users/oracle/Python/Math104A/SolutionOneVariable/')

import OneVariableSolution as OVS
import matplotlib.pyplot as plt
import numpy as np

expression = "x**2-3"
error = 10e-4

p_out = OVS.bisection(0,2,expression,error)
print("Final Guess = " + str(p_out))

x = np.arange(0, 2, 0.01)
y = eval(expression)
plt.plot(x, y)

plt.title('Homework 3 Problem 2.1 - 12')
plt.grid(True)
plt.savefig("2_1_12.png")
plt.show()
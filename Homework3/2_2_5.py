#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 17:52:22 2016

@author: Nathan A Cheadle
"""

import sys
sys.path.insert(0, '/Users/oracle/Python/Math104A/SolutionOneVariable/')

import OneVariableSolution as OVS
import matplotlib.pyplot as plt
import numpy as np

expression = "(3*x**2+3)**(1/4)"
error = 10e-2

p_out = OVS.fixedpoint(1, expression, error)
#print("Final Guess = " + str(p_out))

equation = "x**4-3*x**2-3"
x = np.arange(-3, 3, 0.01)
y = eval(equation)
plt.plot(x, y)

plt.title('Homework 3 Problem 2.2 - 5')
plt.grid(True)
plt.savefig("2_2_5.png")
plt.show()
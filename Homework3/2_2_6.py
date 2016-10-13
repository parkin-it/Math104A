#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 18:35:38 2016

@author: Nathan A Cheadle
"""
import sys
sys.path.insert(0, '/Users/oracle/Python/Math104A/SolutionOneVariable/')

import OneVariableSolution as OVS
import matplotlib.pyplot as plt
import numpy as np

expression = "np.pi+0.5*np.sin(x/2)"
error = 10e-2

p_out = OVS.fixedpoint(np.pi, expression, error)
#print("Final Guess = " + str(p_out))

equation = "x**3-x-1"
x = np.arange(-3, 3, 0.01)
y = eval(equation)
plt.plot(x, y)

plt.title('Homework 3 Problem 2.2 - 6')
plt.grid(True)
plt.savefig("2_2_6.png")
plt.show()
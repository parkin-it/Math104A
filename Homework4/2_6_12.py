#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 17:46:51 2016

@author: Nathan A Cheadle
"""

import sys
sys.path.insert(0, '/Users/oracle/Python/Math104A/SolutionOneVariable/')

import OneVariableSolution as OVS
import numpy as np

x=1/60
fib = 1+22*x+7*x**2+42*x**3+33*x**4+4*x**5+40*x**6

print(fib)

equation = "x**3+2*x**2+10*x-20"
derivative = "3*x**2+4*x+10"
guess = fib

p_out = OVS.newton(guess,equation,derivative,10e-15)
print(p_out)

print(abs(fib-p_out))
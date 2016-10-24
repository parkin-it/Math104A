#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 17:15:12 2016

@author: Nathan A Cheadle
"""

import sys
sys.path.insert(0, '/Users/oracle/Python/Math104A/SolutionOneVariable/')

import OneVariableSolution as OVS
import numpy as np

equation = "600*x**4-550*x**3+200*x**2-20*x-1"
derivative = "2400*x**3-1650*x**2+400*x-20"

print("----Bisection Method----")

p_out = OVS.bisection(0.1,1,equation,10e-4)
print("Final result = " + str(p_out))

print("----Newton's Method----")

p_out = OVS.newton(.55,equation,derivative,10e-4)
print("Final result = " + str(p_out))

print("----Netwon-Secant Method----")

p_out = OVS.newtonSecant(0.1,1,equation,10e-4)
print("Final result = " + str(p_out))

print("----False Proposition Method----")

p_out = OVS.newtonFalse(0.1,1,equation,10e-4)
print("Final result = " + str(p_out))
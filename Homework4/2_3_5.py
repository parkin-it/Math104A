#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 16:45:59 2016

@author: Nathan A Cheadle
"""

import sys
sys.path.insert(0, '/Users/oracle/Python/Math104A/SolutionOneVariable/')

import OneVariableSolution as OVS
import numpy as np

print("--------------A---------------")
p_out = OVS.newton(2, "x**3-2*x**2-5", "3*x**2-4*x", 10e-4)
print("Final Guess = " + str(p_out))

print("--------------B---------------")
p_out = OVS.newton(-2.5, "x**3+3*x**2-1", "3*x**2+6*x", 10e-4)
print("Final Guess = " + str(p_out))

print("--------------C---------------")
p_out = OVS.newton(np.pi/4, "x-np.cos(x)", "1+np.sin(x)", 10e-4)
print("Final Guess = " + str(p_out))

print("--------------D---------------")
p_out = OVS.newton(np.pi/4, "x-.8-.2*np.sin(x)", "1-0.2*np.cos(x)", 10e-4)
print("Final Guess = " + str(p_out))
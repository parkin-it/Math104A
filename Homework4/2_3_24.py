#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 14:47:52 2016

@author: Nathan A Cheadle
"""

import sys
sys.path.insert(0, '/Users/oracle/Python/Math104A/SolutionOneVariable/')

import OneVariableSolution as OVS
import numpy as np

p_out = OVS.newton(1,"1000000*np.exp(x)+(435000/x)*(np.exp(x)-1)-1564000","1000000*np.exp(x)-(435000/x**2)*(np.exp(x)-1)+(435000/x)*(np.exp(x))",10e-4)
print("Final Guess = " + str(p_out))

x = p_out
t = 2

year2 = 1000000*np.exp(t*x)+(435000/(t*x)*(np.exp(t*x)-1))
print("Population at year 2: "+str(year2))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 17:24:34 2016

@author: Nathan A Cheadle
"""

import sys
sys.path.insert(0, '/Users/oracle/Python/Math104A/SolutionOneVariable/')

import OneVariableSolution as OVS
import numpy as np

material = "2*np.pi*(x+.25)**2+(2000*(x+.25))/x**2"

equation = "2*np.pi*(2*x+.5)-2000/x**2-1000/x**3"
derivative = "4*np.pi+4000/x**3+3000/x**4"

p_out = OVS.newton(10,equation,derivative,10e-4)
print("Final result = " + str(p_out))

print("Minimum material needed = " + str(OVS.f_x(material,p_out)))